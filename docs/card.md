## *class* `card.`**`credit`**`(number)` { #card.credit data-toc-label='card.credit' }

!!! abstract "This tool checks the validity and network of a credit card number."

    ```python linenums="1"
    import coreutil

    card = coreutil.card.credit('378282246310005')
    ```

### `credit.`**`isvalid`**`()` { #credit.isvalid data-toc-label='credit.isvalid' }

!!! abstract "Check card number against Luhn Algorithm to see the validity."

    Return `True` if valid, otherwise `False` if invalid.

    ```python linenums="1"
    print(card.isvalid())
    ```
    ```
    True
    ```

### `credit.`**`network`**`()` { #credit.network data-toc-label='credit.network' }

!!! abstract "Determine the credit card network of a card number."

    Return `short` name and `brand` name.

    ```python linenums="1"
    print(card.network())
    ```
    ```
    Network(short='amex', brand='American Express')
    ```

    <sub>:credit_card: &ensp; American Express • Diners Club • Discover • JCB • Maestro • Mastercard • UnionPay • Visa </sub>