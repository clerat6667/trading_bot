from bot.logging_config import logger


def place_order(
    client,
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    try:

        logger.info(
            f"Request => "
            f"Symbol={symbol}, "
            f"Side={side}, "
            f"Type={order_type}, "
            f"Qty={quantity}, "
            f"Price={price}"
        )

        if order_type == "MARKET":

            response = client.market_order(
                symbol,
                side,
                quantity
            )

        else:

            response = client.limit_order(
                symbol,
                side,
                quantity,
                price
            )

        logger.info(f"Response => {response}")

        return response

    except Exception as e:

        logger.error(str(e))

        raise
