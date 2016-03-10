import bpy

bl_info = {'name': 'Screen Pie Menu',
           'description': 'Select screen using pie menu.',
           'author': 'miniukof',
           'version': (0, 0, 2),
           'blender': (2, 76, 11),
           'category': 'User Interface',
           'wiki_url': 'https://github.com/miniukof/bl-screen_pie'
          }

class ScreenPieMenu(bpy.types.Menu):
    bl_label = 'Screen Pie Menu'
    bl_idname = 'ui.screen_pie_menu'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        for i, scr in enumerate(bpy.data.screens):
            if i >= 7:
                break
            pie.operator(ScreenPieChange.bl_idname,
                         text=scr.name).scr_name = scr.name

class ScreenPieChange(bpy.types.Operator):
    bl_idname = 'pie.screen_pie_menu_change_screen'
    bl_label = 'Change Screen Function for ScreenPieMenu'

    scr_name = bpy.props.StringProperty()

    def execute(self, context):
        bpy.context.window.screen = bpy.data.screens[self.scr_name]
        return{'FINISHED'}

def register():
    bpy.utils.register_class(ScreenPieMenu)
    bpy.utils.register_class(ScreenPieChange)

def unregister():
    bpy.utils.unregister_class(ScreenPieMenu)
    bpy.utils.unregister_class(ScreenPieChange)
