# Generated by Django 4.0.2 on 2022-03-14 00:08

from django.db import migrations, models
import django.db.models.deletion
import page.blocks
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('hero_image', wagtail.core.blocks.StructBlock([('hero_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('hero_heading', wagtail.core.blocks.CharBlock(help_text='40 character limit.', max_length=140, required=False)), ('hero_message', wagtail.core.blocks.CharBlock(help_text='140 character limit.', max_length=140, required=False)), ('hero_photo_credit', wagtail.core.blocks.CharBlock(help_text='80 character limit. This will show on the bottom right on the image', max_length=80, required=False)), ('hero_cta', wagtail.core.blocks.CharBlock(help_text='Text to display on Call to Action. 20 character limit.', max_length=20, required=False, verbose_name='Hero CTA'))], icon='image')), ('single_column', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image', 'code', 'ol'], icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('document_block', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))]))])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('background_color', page.blocks.BackgroundColorBlock(default='normal', required=False))], group='COLUMNS')), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image', 'code', 'ol'], icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('document_block', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))]))])), ('right_column', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image', 'code', 'ol'], icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('document_block', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))]))])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('background_color', page.blocks.BackgroundColorBlock(default='normal', required=False))], group='COLUMNS')), ('three_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image', 'code', 'ol'], icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('document_block', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))]))])), ('middle_column', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image', 'code', 'ol'], icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('document_block', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))]))])), ('right_column', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image', 'code', 'ol'], icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('document_block', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))]))])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('background_color', page.blocks.BackgroundColorBlock(default='normal', required=False))], group='COLUMNS')), ('four_columns', wagtail.core.blocks.StructBlock([('left_column_1', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image', 'code', 'ol'], icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('document_block', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))]))])), ('left_column_2', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image', 'code', 'ol'], icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('document_block', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))]))])), ('right_column_1', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image', 'code', 'ol'], icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('document_block', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))]))])), ('right_column_2', wagtail.core.blocks.StreamBlock([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image', 'code', 'ol'], icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('border', wagtail.core.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.core.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))])), ('document_block', wagtail.core.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome')])), ('name', wagtail.core.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.core.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))]))])), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], requirement=False)), ('background_color', page.blocks.BackgroundColorBlock(default='normal', required=False))], group='COLUMNS')), ('image_grid', wagtail.core.blocks.StreamBlock([('grid', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.core.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.core.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))]))], help_text='Minimum 2 blocks and a maximum of 4 blocks', icon='image', max_num=4, min_num=2))], default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
