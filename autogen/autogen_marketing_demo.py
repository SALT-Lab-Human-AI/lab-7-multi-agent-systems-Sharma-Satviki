"""
AutoGen Multi-Agent Workflow: Product Marketing Strategy

This is a 5-phase workflow using ConversableAgents for:
1. Market Research
2. Customer Analysis
3. Strategy Creation
4. Campaign Design
5. Quality Refinement

Plug-and-play structure matching your existing SimpleInterviewPlatformWorkflow.
"""

from datetime import datetime
from config import Config
from openai import OpenAI


class MarketingStrategyWorkflow:
    """Marketing Strategy Multi-Agent Workflow"""

    def __init__(self, product_name="SmartHealth Fitness Band"):
        if not Config.validate_setup():
            print("ERROR: Configuration validation failed!")
            exit(1)

        self.client = OpenAI(api_key=Config.API_KEY, base_url=Config.API_BASE)
        self.outputs = {}
        self.model = Config.OPENAI_MODEL
        self.product_name = product_name

    # ---------------------------------------------------------
    # RUN WORKFLOW
    # ---------------------------------------------------------
    def run(self):
        print("\n" + "="*80)
        print("AUTOGEN MARKETING STRATEGY WORKFLOW")
        print("="*80)
        print(f"Product: {self.product_name}")
        print(f"Model: {self.model}")
        print(f"Start Time: {datetime.now()}\n")

        self.phase_market_research()
        self.phase_customer_analysis()
        self.phase_strategy()
        self.phase_campaigns()
        self.phase_quality()

        self.print_summary()

    # ---------------------------------------------------------
    # PHASE 1 — MARKET RESEARCH
    # ---------------------------------------------------------
    def phase_market_research(self):
        print("\n" + "="*80)
        print("PHASE 1: MARKET RESEARCH")
        print("="*80)

        system_prompt = f"""
You are a senior market research analyst.
Analyze the wearable technology market for the product: {self.product_name}.

Provide:
- Top 3 competitors
- Their positioning
- Pricing
- Key features
- Market trends
Limit to 150–200 words.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.7,
            max_tokens=500,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": "Provide competitor analysis."}
            ]
        )

        self.outputs["market_research"] = response.choices[0].message.content
        print(self.outputs["market_research"])

    # ---------------------------------------------------------
    # PHASE 2 — CUSTOMER INSIGHTS
    # ---------------------------------------------------------
    def phase_customer_analysis(self):
        print("\n" + "="*80)
        print("PHASE 2: CUSTOMER INSIGHTS")
        print("="*80)

        system_prompt = f"""
You are a consumer behavior expert.
Based on the market research, identify:

- Target customer segments
- User pain points
- Motivations
- Purchase triggers
- Unmet needs

Limit to 150 words.
"""

        user_prompt = f"Here is the market research:\n{self.outputs['market_research']}\n\nAnalyze customers."

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.7,
            max_tokens=400,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        self.outputs["customer_analysis"] = response.choices[0].message.content
        print(self.outputs["customer_analysis"])

    # ---------------------------------------------------------
    # PHASE 3 — MARKETING STRATEGY
    # ---------------------------------------------------------
    def phase_strategy(self):
        print("\n" + "="*80)
        print("PHASE 3: MARKETING STRATEGY")
        print("="*80)

        system_prompt = f"""
You are a marketing strategist.
Create a marketing strategy for: {self.product_name}

Include:
- Positioning statement
- Value proposition
- Key messaging pillars
- Channels to target
- Pricing strategy
- Brand voice direction

Limit to 200 words.
"""

        user_prompt = f"""
Market Research:
{self.outputs['market_research']}

Customer Insights:
{self.outputs['customer_analysis']}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.7,
            max_tokens=500,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        self.outputs["strategy"] = response.choices[0].message.content
        print(self.outputs["strategy"])

    # ---------------------------------------------------------
    # PHASE 4 — CAMPAIGN DESIGN
    # ---------------------------------------------------------
    def phase_campaigns(self):
        print("\n" + "="*80)
        print("PHASE 4: CAMPAIGN DESIGN")
        print("="*80)

        system_prompt = """
You are a creative campaign director.
Design 3 marketing campaigns:

1. Digital campaign
2. Influencer campaign
3. Content/SEO campaign

Include:
- Goal
- Target channels
- Creative concept
- KPIs
Keep each campaign short and crisp.
"""

        user_prompt = f"""
Based on the marketing strategy:

{self.outputs['strategy']}

Generate the 3 campaigns.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.7,
            max_tokens=500,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        self.outputs["campaigns"] = response.choices[0].message.content
        print(self.outputs["campaigns"])

    # ---------------------------------------------------------
    # PHASE 5 — QUALITY POLISHING
    # ---------------------------------------------------------
    def phase_quality(self):
        print("\n" + "="*80)
        print("PHASE 5: QUALITY REVIEW")
        print("="*80)

        system_prompt = """
You are a quality editor. Improve clarity, flow, and formatting.
Combine all sections into a polished executive summary.
Max 250 words.
"""

        user_prompt = f"""
Market Research:
{self.outputs['market_research']}

Customer Insights:
{self.outputs['customer_analysis']}

Marketing Strategy:
{self.outputs['strategy']}

Campaigns:
{self.outputs['campaigns']}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.5,
            max_tokens=500,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        self.outputs["quality"] = response.choices[0].message.content
        print(self.outputs["quality"])

    # ---------------------------------------------------------
    # SUMMARY
    # ---------------------------------------------------------
    def print_summary(self):
        print("\n" + "="*80)
        print("FINAL SUMMARY — MARKETING STRATEGY")
        print("="*80)

        for key, value in self.outputs.items():
            print(f"\n--- {key.upper()} ---\n")
            print(value)


if __name__ == "__main__":
    workflow = MarketingStrategyWorkflow(product_name="SmartHealth Fitness Band")
    workflow.run()
