"""Create beautiful fractal images."""
from PIL import Image


class Fractal:
    """Fractal class."""

    def __init__(self, size, scale, computation, max_iter=1000, escape_radius=2):
        """
        Initialize fractal.

        Arguments:
        size -- the size of the image as a tuple (x, y)
        scale -- the scale of x and y as a list of 2-tuple
                 [(minimum_x, minimum_y), (maximum_x, maximum_y)]
                 these are mathematical coordinates
        computation -- the function used for computing pixel values
        max_iter -- maximum number of iterations (default: 1000)
        escape_radius -- escape radius for the fractal (default: 2)
        """
        self.size = size
        self.scale = scale
        self.computation = computation
        self.max_iter = max_iter
        self.escape_radius = escape_radius

    def compute(self):
        """Create the fractal by computing every pixel value."""
        width, height = self.size
        image = Image.new("L", self.size)
        pixels = image.load()

        for px in range(width):
            for py in range(height):
                # Map pixel to mathematical coordinates
                x_min, y_min = self.scale[0]
                x_max, y_max = self.scale[1]
                x = x_min + (px / width) * (x_max - x_min)
                y = y_min + (py / height) * (y_max - y_min)

                # Compute pixel value
                iterations = self.pixel_value((x, y))
                # Map iterations to grayscale (0 to 255)
                color = int(255 * iterations / self.max_iter)
                pixels[px, py] = color

        return image

    def pixel_value(self, pixel):
        """
        Return the number of iterations it took for the pixel to go out of bounds.

        Arguments:
        pixel -- the pixel coordinate (x, y)

        Returns:
        the number of iterations of computation it took to go out of bounds as integer.
        """
        x, y = pixel
        x0, y0 = x, y
        for i in range(self.max_iter):
            x, y = self.computation(x, y, x0, y0)
            if x**2 + y**2 > self.escape_radius**2:
                return i
        return self.max_iter

    def save_image(self, filename):
        """
        Save the image to hard drive.

        Arguments:
        filename -- the file name to save the file to as a string.
        """
        image = self.compute()
        image.save(filename)

def mandelbrot_computation(x, y, x_original, y_original):
    """
    Mandelbrot computation: z = z^2 + c.
    """
    return x**2 - y**2 + x_original, 2 * x * y + y_original

def julia_computation(x, y, x_original, y_original):
    """
    Julia computation: z = z^n + c (n=3, c fixed).
    """
    c = -0.7869 + 0.1889j  # Constant for Julia set
    n = 3
    z = complex(x, y)
    z = z**n + c
    return z.real, z.imag

def ship_computation(x, y, x_original, y_original):
    """
    Burning Ship computation: z = (|Re(z)| + i|Im(z)|)^2 + c.
    """
    x, y = abs(x), -abs(y)
    return x**2 - y**2 + x_original, 2 * x * y + y_original


if __name__ == "__main__":
    size = (1000, 1000)
    used_arguments = f"size_{size}_"
    
    mandelbrot = Fractal(size, [(-2, -2), (2, 2)], mandelbrot_computation)
    mandelbrot.compute()
    mandelbrot.save_image(used_arguments + "mandelbrot.png")
    print("Mandelbrot image generation completed.")
    
    mandelbrot2 = Fractal(size, [(-0.74877, 0.065053), (-0.74872, 0.065103)], mandelbrot_computation)
    mandelbrot2.compute()
    mandelbrot2.save_image(used_arguments + "mandelbrot2.png")
    print("Mandelbrot2 image generation completed.")
    
    julia = Fractal(size, [(-2, -2), (2, 2)], julia_computation)
    julia.compute()
    julia.save_image(used_arguments + "julia.png")
    print("Julia image generation completed.")

    ship = Fractal(size, [(-2, -2), (2, 2)], ship_computation)
    ship.compute()
    ship.save_image(used_arguments + "ship.png")
    print("Ship image generation completed.")
