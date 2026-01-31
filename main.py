import arcade

arcade.Window(800, 600, "Game")
arcade.start_render()
arcade.draw_ellipse_filled(200, 300, 100, 40, arcade.color.AERO_BLUE)
arcade.draw_arc_outline(120, 120, 200, 150, arcade.color.WHITE, 30, 190)
arcade.finish_render()
arcade.run()