def query():
    query_ = """
        CREATE TABLE IF NOT EXISTS transactions AS SElECT * FROM ledger;
        """
    return query_


def query1():
    query1_ = """
        CREATE TABLE IF NOT EXISTS budget AS SELECT * FROM budget;
        """
    return query1_


def query_inc(x):
    # income
    query3_ = f"""
        SELECT SUM(AMOUNT) FROM transactions 
        WHERE BUDGET_LINE = {x + 5}
        """
    return query3_


def query_exp(x):
    # Expenses
    query_sumt_ = f"""
        SELECT SUM(AMOUNT) FROM transactions 
        WHERE BUDGET_LINE = {x}
        """
    return query_sumt_


def query_bud(x):
    query_sum_ = f"""
        SELECT BUDGET FROM budget
        WHERE BUDGET_LINE = {x}
        """
    return query_sum_
