from manim import *
from manim.opengl import *

class Precession(ThreeDScene):
	def create_spin(self, phase: float, cone: Circle):
		spin = Arrow3D(start=[0, 0, 0], end=[cone.radius * np.cos(phase), cone.radius * np.sin(phase), cone.get_z()])
		return spin

	def create_more_spins(self, n: int, cone):
		# angles = [360. / i for i in range(n)]
		return VGroup(*[self.create_spin(i * 360 * DEGREES / n, cone=cone) for i in range(n)])


	def construct(self):
		cone_top = Circle(radius=1)
		cone_bottom = Circle(radius=1)

		cone_top.shift(2 * OUT)
		cone_bottom.shift(2 * IN)

		self.cone_top = cone_top
		self.cone_bottom = cone_bottom

		

		spins_top = self.create_more_spins(3, self.cone_top)
		self.add(spins_top)
		self.add(cone_top)


		spins_bottom = self.create_more_spins(3, self.cone_bottom)
		self.add(spins_bottom)
		self.add(cone_bottom)



		self.set_camera_orientation(phi=70 * DEGREES)


		self.play(
			Rotate(spins_top, angle=2 * PI, about_point=[0, 0, 1]),
			Rotate(spins_bottom, angle=2 * PI, about_point=[0, 0, 1]),
			run_time=2
		)
		self.move_camera(phi=0)
		self.wait()
		# self.play(Rotate(spins_bottom, angle=2 * PI, about_point=[0, 0, 1]), run_time=4)


class OpenGLIntro(Scene):
    def construct(self):
        hello_world = Tex("Hello World!").scale(3)
        self.play(Write(hello_world))
        self.play(
            self.camera.animate.set_euler_angles(
                theta=-10*DEGREES,
                phi=50*DEGREES
            )
        )
        self.play(self.camera.animate.set_euler_angles(theta=60*DEGREES))