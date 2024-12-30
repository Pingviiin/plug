from PIL import Image

class Fractal:
    """Fractal class."""

    def __init__(self, size, scale, computation):
        self.size = size
        self.scale = scale
        self.computation = computation
        self.image = Image.new("RGB", size)

    def compute(self):
        width, height = self.size
        pixels = self.image.load()

        for px in range(width):
            for py in range(height):
                # Map pixel coordinates to mathematical coordinates
                x_math = self.scale[0][0] + px / width * (self.scale[1][0] - self.scale[0][0])
                y_math = self.scale[0][1] + py / height * (self.scale[1][1] - self.scale[0][1])
                iterations = self.pixel_value((x_math, y_math))

                # Map iterations to RGB color
                color = (iterations % 256, iterations % 256, iterations % 256) if iterations < 255 else (0, 0, 0)
                pixels[px, py] = color

    def pixel_value(self, pixel):
        x, y = pixel
        x0, y0 = x, y
        max_iterations = 255

        for i in range(max_iterations):
            x, y = self.computation(x, y, x0, y0)
            if x * x + y * y > 4:  # Escape condition
                return i
        return max_iterations

    def save_image(self, filename):
        self.image.save(filename)


def mandelbrot_computation(x, y, x_original, y_original):
    z_real, z_imag = x, y
    c_real, c_imag = x_original, y_original

    z_real_new = z_real * z_real - z_imag * z_imag + c_real
    z_imag_new = 2 * z_real * z_imag + c_imag

    return z_real_new, z_imag_new


def julia_computation(x, y, x_original, y_original):
    c_real, c_imag = -0.7869, 0.1889

    z_real_new = x * x - y * y + c_real
    z_imag_new = 2 * x * y + c_imag

    return z_real_new, z_imag_new


def ship_computation(x, y, x_original, y_original):
    z_real, z_imag = abs(x), -abs(y)  # Invert y-axis
    c_real, c_imag = x_original, y_original

    z_real_new = z_real * z_real - z_imag * z_imag + c_real
    z_imag_new = 2 * z_real * z_imag + c_imag

    return z_real_new, z_imag_new



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
