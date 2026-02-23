from decimal import Decimal
import sys


def format_ms(total_ms: Decimal):
    hours = total_ms // 3_600_000
    remaining = total_ms % 3_600_000

    minutes = remaining // 60_000
    remaining %= 60_000

    seconds = remaining // 1_000
    milliseconds = remaining % 1_000

    if hours > 0:
        return f"{hours}:{minutes}:{seconds}.{milliseconds}"
    elif minutes > 0:
        return f"{minutes}:{seconds}.{milliseconds}"
    else:
        return f"{seconds}.{milliseconds}"


def main() -> int:
    if len(sys.argv) != 4:
        print("Usage: python3 frame-count.py <FPS> <START_FRAME> <END_FRAME>")
        return 1

    try:
        fps = int(sys.argv[1])
        start = int(sys.argv[2])
        end = int(sys.argv[3])
    except Exception:
        print("The values entered must be numbers.")
        print("Usage: python3 frame-count.py <FPS> <START_FRAME> <END_FRAME>")
        return 1

    milliseconds = (Decimal(end - start) * Decimal(1000) / Decimal(fps)).quantize(
        Decimal("1")
    )
    print(format_ms(milliseconds))

    return 0


if __name__ == "__main__":
    exit(main())
