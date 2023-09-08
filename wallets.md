A company hosts a cryptocurrency exchange platform. They have an admin portal that interacts with a postgreSQL database that stores the history/ledger of exchanges/transactions.

The database has the schema below:

|  | TRANSACTIONS |  |
|---|---|---|
| NAME | TYPE | DESCRIPTION |
| dt | timestamp | datetime |
| sender | varchar(42) | |
| recipient | varchar(42) | |
| amount | Decimal(10, 6) | |

Example database table:
| Sender | Recipient | dt | amount |
| --- | --- | --- | --- |
| 0xf82... | 0xg56... | 2021.04.05.19:56:02 | 120.35 |
| 0xd78... | 0xfd4... | 2021.05.06.05:21:20 | 32.52 |

Create a query that returns the list of addresses, the number of outgoing and incoming transactions and the balance of Ethereuem cold wallets calcualated based on movement of funds between these wallets in 2021.

Results should have their columns as:
| wallet | outgoing | incoming | balance |
| -- | -- | -- | -- |
| | | | |

Results should be sorted in ascending order by wallet. Only transactions in 2021 are to be included.

```sql
WITH ColdWallets AS (
    SELECT DISTINCT sender AS wallet
    FROM TRANSACTIONS
    WHERE EXTRACT(YEAR FROM dt) = 2021
    
    UNION
    
    SELECT DISTINCT recipient AS wallet
    FROM TRANSACTIONS
    WHERE EXTRACT(YEAR FROM dt) = 2021
) 

SELECT
    c.wallet,
    COALESCE(OutgoingCount, 0) AS outgoing,
    COALESCE(IncomingCount, 0) AS incoming,
    COALESCE(IncomingSum, 0) - COALESCE(OutgoingSum, 0) AS balance
FROM ColdWallets c
LEFT JOIN (
    SELECT sender, COUNT(*) AS OutgoingCount, SUM(amount) AS OutgoingSum
    FROM TRANSACTIONS
    WHERE EXTRACT(YEAR FROM dt) = 2021
    GROUP BY sender
) Outgoing ON c.wallet = Outgoing.sender
LEFT JOIN (
    SELECT recipient, COUNT(*) AS IncomingCount, SUM(amount) AS IncomingSum
    FROM TRANSACTIONS
    WHERE EXTRACT(YEAR FROM dt) = 2021
    GROUP BY recipient
) Incoming ON c.wallet = Incoming.recipient

ORDER BY c.wallet;

```

### Explanations
- Get a distinct list of all wallet addresses involved in transactions in 2021, combining (hence `UNION`) the set of outgoing and incoming into a single set of transactions.
- For each wallet transaction, use subqueries to calculate the number of outgoing transactions, incoming transactions and the balance for each. We use `JOIN` to ensure we capture wallet transactions in which only incoming or outgoing transactions were involved. `COALESCE` ensures that default to zero, the count and sum of wallet which have no outgoing or incoming transactions.
