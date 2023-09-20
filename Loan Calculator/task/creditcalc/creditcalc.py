import math
import argparse


def calculate_principal(annual_interest, payment, periods):
    interest = annual_interest / (12 * 100)

    numerator = interest * pow(interest + 1, periods)
    denominator = pow(interest + 1, periods) - 1
    total_interest = numerator / denominator
    loan_principal = payment / total_interest
    print(f"Your loan principal = {math.ceil(loan_principal)}!")
    print(f"Overpayment = {(periods * payment) - math.ceil(loan_principal)}")


def calculate_annuity_payment(annual_interest, loan_principal, periods):
    interest = annual_interest / (12 * 100)

    numerator = interest * pow(interest + 1, periods)
    denominator = pow(interest + 1, periods) - 1
    ordinary_annuity = math.ceil(loan_principal * (numerator / denominator))
    print(f"Your annuity payment = {math.ceil(ordinary_annuity)}!")
    print(f"Overpayment = {(periods * ordinary_annuity) - math.ceil(loan_principal)}")


def calculate_months(annual_interest, loan_principal, monthly_payment):
    nominal_interest = annual_interest / (12 * 100)

    # Intermediate calculations
    interest_factor = nominal_interest + 1
    payment_difference = monthly_payment - (nominal_interest * loan_principal)

    # Final calculation
    months = math.ceil(math.log(monthly_payment / payment_difference, interest_factor))
    if months % 12 == 0:
        years = int(months / 12)
        print(f"It will take {years} year{'s' if years > 1 else ''} to repay this loan!")
    elif months < 12:
        print(f"It will take {months} month{'s' if months > 1 else ''} to repay this loan!")
    else:
        years = int(months / 12)
        months = int(months % 12)
        print(f"It will take {years} year{'s' if years > 1 else ''} "
              f"and {months} month{'s' if months > 1 else ''} to repay this loan!")
    print(f"Overpayment = {(int(monthly_payment * months) - math.ceil(loan_principal))}")

def compute_diff_payments(annual_interest, loan_principal, periods):
    interest = annual_interest / (12 * 100)
    counter = 0
    for period in range(periods):
        period += 1
        numerator = loan_principal * (period - 1)
        right_side = interest * (loan_principal - (numerator / periods))
        left_side = loan_principal / periods
        diff_payment = math.ceil(left_side + right_side)
        counter += diff_payment
        print(f"Month {period}: payment is {diff_payment}")
    print(f"Overpayment = {counter - math.ceil(loan_principal)}")


parser = argparse.ArgumentParser(description="")

parser.add_argument("--type",
                    choices=["diff", "annuity"],
                    help="Incorrect parameters")

parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if args.type == "annuity":
    if not args.interest:
        print("Incorrect parameters")
    else:
        if args.principal is None and args.payment is not None and args.periods is not None:
            interest = float(args.interest)
            payment = float(args.payment)
            periods = int(args.periods)
            calculate_principal(interest, payment, periods)
        elif args.payment is None and args.principal is not None and args.periods is not None:
            interest = float(args.interest)
            principal = float(args.principal)
            periods = int(args.periods)
            calculate_annuity_payment(interest, principal, periods)
        elif args.periods is None and args.principal is not None and args.payment is not None:
            interest = float(args.interest)
            principal = float(args.principal)
            payment = float(args.payment)
            calculate_months(interest, principal, payment)
        else:
            print("Incorrect parameters")

elif args.type == "diff":
    if args.payment or not args.interest:
        print("Incorrect parameters")
    elif args.principal and args.periods:
        interest = float(args.interest)
        principal = float(args.principal)
        periods = int(args.periods)
        compute_diff_payments(interest, principal, periods)
    else:
        print("Incorrect parameters")
