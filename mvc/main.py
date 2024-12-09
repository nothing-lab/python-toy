from lotto_controller import LottoController
from lotto_service import LottoService
from lotto_draw_type import LottoDrawType


def main():
    service = LottoService()
    LottoController(service).run(LottoDrawType.AUTO)


if __name__ == '__main__':
    main()
