from configparser import ConfigParser
from src.main import Extractor
config = ConfigParser()
config.read('config.ini')
config_default = config['DEFAULT']
extractor = Extractor(config_default,'en')


def  extracting(document:str,num_keywords:int):
    return {"keywords": extractor.run(document,num_keywords)}
keywords = extracting("""The US bank may need to raise more funds despite a $30bn rescue last week
Edward Helmore
Mon 20 Mar 2023 19.57 GMT
Shares in troubled First Republic Bank crashed more than 46% on Monday, after reports the San Francisco-based bank may need to raise more funds despite a $30bn (£24bn) rescue last week.

As the growing banking crisis spread into a new week, the credit rating of the regional bank was downgraded deeper into junk status by S&P Global. The agency said that the bank, which caters to wealthy clients, probably faced “high liquidity stress with substantial outflows”.

US officials are studying how to temporarily expand the protection offered to banking customers by Federal Deposit Insurance Corp (FDIC) to include all deposits, going beyond the current $250,000 cap, Bloomberg reported on Monday night.


Like the collapsed Silicon Valley Bank (SVB), a large proportion of First Republic’s customers hold more than the $250,000 amount guaranteed by federal insurance.

However, the move may face political roadblocks. Hardline Republicans in the House of Representatives on Monday vowed to oppose any cover extension.

The Republican House Freedom Caucus said in a statement: “Any universal guarantee on all bank deposits, whether implicit or explicit, enshrines a dangerous precedent that simply encourages future irresponsible behavior to be paid for by those not involved who followed the rules.”

First Republic’s woes follow the collapse of SVB and New York-based Signature. Over the weekend Credit Suisse became the largest institution so far to be embroiled in the upheaval when the Swiss government forced the troubled bank into a cut-price takeover by rival UBS.

First Republic has struggled to reassure depositors that it will not suffer the same fate as SVB and Signature. Last week, the bank increased borrowings from the US Federal Reserve and then suspended its common stock dividend despite holding about $213bn in assets and $176bn in deposits.

UBS and Credit Suisse logos 
UK and US shares climb as banks and ministers aim to calm Credit Suisse fears
Read more
On Sunday, Reuters reported that the lender was still trying to put together a deal to raise capital, days after 11 of the biggest names in US banking, including JPMorgan Chase, Citigroup, Bank of America and Goldman Sachs kicked in $30bn.

Efforts to provide new support to First Republic are being led by the JP Morgan CEO, Jamie Dimon, the Wall Street Journal reported.


In a regulatory filing, the First Republic executive chairman, Jim Herbert, and the CEO, Mike Roffler, said the cash injection “is a vote of confidence for First Republic and the entire US banking system”.

But First Republic’s shares have lost 80% of their value over the past 10 days on fears of a bank run. About 70% of First Republic’s deposits are uninsured, well above a 55% average for medium-sized banks, a figure that puts the bank third after SVB (94%) and Signature Bank (90%), according to Bank of America.""",
    12)
print(keywords)