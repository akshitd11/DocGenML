# docgen/formatter.py
from pathlib import Path
import jinja2
import os
from abc import ABC, abstractmethod
import tempfile
import shutil

class BaseFormatter(ABC):
    """Base class for all formatters"""
    
    @abstractmethod
    def render(self, items, **kwargs):
        """Convert parsed items into the target format"""
        pass
    
    def get_template(self, template_name):
        """Load a Jinja2 template from the templates directory"""
        template_dir = Path(__file__).parent / "templates"
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(str(template_dir)),
            autoescape=jinja2.select_autoescape(['html'])
        )
        return env.get_template(template_name)


class MarkdownFormatter(BaseFormatter):
    """Format parsed items as Markdown"""
    
    def render(self, items, **kwargs):
        template = self.get_template("markdown_template.md")
        return template.render(items=items, **kwargs)


class HtmlFormatter(BaseFormatter):
    """Format parsed items as HTML"""
    
    def render(self, items, **kwargs):
        template = self.get_template("html_template.html")
        return template.render(items=items, **kwargs)


class LaTeXFormatter(BaseFormatter):
    """Format parsed items as LaTeX"""
    
    def render(self, items, **kwargs):
        template = self.get_template("latex_template.tex")
        return template.render(items=items, **kwargs)


class PDFFormatter(BaseFormatter):
    """Format parsed items as PDF (via ReportLab)"""
    
    def render(self, items, **kwargs):
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.lib.styles import getSampleStyleSheet
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
            from reportlab.lib.units import inch
        except ImportError:
            raise ImportError(
                "PDF formatting requires ReportLab. "
                "Install it with 'pip install reportlab'"
            )
            
        # Create a BytesIO object for the PDF
        from io import BytesIO
        buffer = BytesIO()
        
        # Create the PDF document
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        flowables = []
        
        # Add title
        flowables.append(Paragraph("API Documentation", styles['Title']))
        flowables.append(Spacer(1, 0.5*inch))
        
        # Process each item and add to PDF
        for item in items:
            # Handle different types of objects by checking attributes
            # First, try to get the name attribute
            try:
                name = item.name if hasattr(item, 'name') else str(item)
                flowables.append(Paragraph(name, styles['Heading1']))
                flowables.append(Spacer(1, 0.2*inch))
                
                # Add docstring if available
                if hasattr(item, 'docstring') and item.docstring:
                    flowables.append(Paragraph(item.docstring, styles['Normal']))
                    flowables.append(Spacer(1, 0.1*inch))
                
                # Add parameters if available
                if hasattr(item, 'params') and item.params:
                    flowables.append(Paragraph("Parameters:", styles['Heading2']))
                    for param in item.params:
                        if hasattr(param, 'name') and hasattr(param, 'desc'):
                            param_text = f"<b>{param.name}</b>: {param.desc}"
                            flowables.append(Paragraph(param_text, styles['Normal']))
                    flowables.append(Spacer(1, 0.1*inch))
                
                # Add return value if available
                if hasattr(item, 'returns') and item.returns:
                    flowables.append(Paragraph("Returns:", styles['Heading2']))
                    flowables.append(Paragraph(item.returns, styles['Normal']))
                
                flowables.append(Spacer(1, 0.3*inch))
            except Exception as e:
                # Add error handling for problematic items
                flowables.append(Paragraph(f"Error processing item: {str(e)}", styles['Normal']))
                flowables.append(Spacer(1, 0.1*inch))
        
        # Build the PDF
        doc.build(flowables)
        
        # Get the PDF content
        pdf_data = buffer.getvalue()
        buffer.close()
        
        return pdf_data


def get_formatter(format_name):
    """Factory function to get the appropriate formatter"""
    formatters = {
        'markdown': MarkdownFormatter,
        'md': MarkdownFormatter,
        'html': HtmlFormatter,
        'latex': LaTeXFormatter,
        'tex': LaTeXFormatter,
        'pdf': PDFFormatter
    }
    
    if format_name.lower() not in formatters:
        raise ValueError(
            f"Unsupported format: {format_name}. "
            f"Supported formats: {', '.join(formatters.keys())}"
        )
    
    return formatters[format_name.lower()]()