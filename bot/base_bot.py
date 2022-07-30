import sc2

from sc2.bot_ai import BotAI


class BaseBot(BotAI):
    def get_xyz(self, point):
        if isinstance(point, sc2.position.Point3):
            x, y, z = point
        elif isinstance(point, sc2.position.Point2):
            x, y, z = (*point, self.get_terrain_z_height(point))
        elif isinstance(point, tuple) and len(point) == 2:
            point = sc2.position.Point2(point)
            x, y, z = (*point, self.get_terrain_z_height(point))
        elif isinstance(point, list) and len(point) == 2:
            point = sc2.position.Point2(point)
            x, y, z = (*point, self.get_terrain_z_height(point))
        elif (
                isinstance(point, list) and len(point) == 3
                or isinstance(point, tuple) and len(point) == 3
        ):
            x, y, z = point
        else:
            raise NotImplementedError("get_xyz not implemented for this type")

        return (x, y, z)

    def draw_sphere(self, position, radius=1, color=(255, 255, 255)):
        x, y, z = self.get_xyz(position)
        position = sc2.position.Point3((x, y, z))

        self.client.debug_sphere_out(
            p=position,
            r=radius,
            color=color
        )

    def draw_box(self, position, radius, color=(255, 255, 255)):
        x, y, z = self.get_xyz(position)
        position = sc2.position.Point3((x, y, z))

        self.client.debug_box2_out(
            pos=position,
            half_vertex_length=radius,
            color=color
        )

    def draw_line(self, start, end, color=(255, 255, 255)):
        x, y, z = self.get_xyz(start)
        start = sc2.position.Point3((x, y, z + 0.1))

        x, y, z = self.get_xyz(end)
        end = sc2.position.Point3((x, y, z + 0.1))

        self.client.debug_line_out(
            p0=start,
            p1=end,
            color=color
        )

    def draw_text(self, text, position, color=(255, 255, 255), size=12):
        x, y, z = self.get_xyz(position)
        position = sc2.position.Point3((x, y, z))

        self.client.debug_text_world(
            text=text,
            pos=position,
            color=color,
            size=size
        )

    def draw_text_info(self, entries, position, x_offset=2.5):
        x, y, z = self.get_xyz(position)

        range_offset = int(x_offset * 10)

        for y_offset, entry in zip(
            range(range_offset, -range_offset, -5),
            entries
        ):
            y_offset /= 10

            entry_text, entry_color = entry

            text_position = sc2.position.Point3((
                x + x_offset,
                y + y_offset,
                z
            ))
            self.draw_text(entry_text, text_position, entry_color)

    def draw_screen_text(self, text, position, color=None, size=12):
        self.client.debug_text_screen(
            text=text,
            pos=position,
            color=color,
            size=size
        )
