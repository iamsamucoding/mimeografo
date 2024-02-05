import json
import io

import seaborn as sns
import matplotlib.pyplot as plt


def plot_data(df, plot, x_var, y_var, hue_var, chart_kargs):
    plot_args = {}
    if x_var:
        plot_args["x"] = x_var
    if y_var:
        plot_args["y"] = y_var
    if hue_var:
        plot_args["hue"] = hue_var
    
    chart_kargs_dict = {}
    plt_kargs = {}
    sns_kargs = {}
    if chart_kargs:
        chart_kargs_dict = json.loads(chart_kargs)
        if "plt" in chart_kargs_dict:
            plt_kargs = chart_kargs_dict["plt"]
        if "sns" in chart_kargs_dict:
            sns_kargs = chart_kargs_dict["sns"]
            plot_args.update(sns_kargs)

    fig, ax = plt.subplots(figsize=(10, 2))
    if plot == "Bar Plot":
        sns.barplot(data=df, ax=ax, **plot_args)
    elif plot == "Line Plot":
        sns.lineplot(data=df, ax=ax, **plot_args)
    elif plot == "Scatter Plot":
        sns.scatterplot(data=df, ax=ax, **plot_args)
    ax.set(**plt_kargs)
    # ax.grid(plt_kargs.get("grid", False))
    
    return fig

def make_slide(presentation, template_slide, title, subtitle, fig):
    if template_slide == 'Template 1':
        make_slide_template_1(presentation, title, subtitle, fig)
    return presentation

def make_slide_template_1(presentation, title, subtitle, fig):
    print(fig.dpi, fig.get_size_inches(), fig.get_size_inches() * fig.dpi)
    print('[1]')
    slide = presentation.slides.add_slide(presentation.slide_layouts[0])
    print(title, subtitle)
    slide.shapes[0].text = title
    slide.shapes[1].text = subtitle
    pic = slide.shapes[2]
    left = pic.left
    top = pic.top
    width = pic.width
    height = pic.height
    print('[4]')
    # Remove the picture
    slide.shapes._spTree.remove(pic._element)
    print('[5]')
    image_stream = io.BytesIO()
    plt.savefig(image_stream)
    
    slide.shapes.add_picture(image_stream, left, top, width, height)
    
    # replace_paragraph_text_retaining_initial_formatting(title_paragraph, title)
    print('[6]')
    # replace_paragraph_text_retaining_initial_formatting(subtitle_paragraph,
                                                        # subtitle)
    print('[7]')
    
    return slide
