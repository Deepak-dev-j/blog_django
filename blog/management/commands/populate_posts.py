from typing import Any
from blog.models import Post,Category
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help = "This command populates the database with sample blog posts."
    def handle(self, *args: Any, **options: Any):
        # data delete exisit data
        Post.objects.all().delete()
        # 

        titles = [
                    "The Future of AI",
                    "Climate Change Solutions",
                    "Remote Work Trends",
                    "Quantum Computing Explained",
                    "Renewable Energy Innovations",
                    "Robotics Advancements",
                    "Deep Learning Demystified",
                    "Post-Pandemic Economic Outlook",
                    "Blockchain in Finance",
                    "Storytelling in Marketing",
                    "Medical Technology Advances",
                    "Space Exploration Challenges",
                    "Psychology of Decision Making",
                    "Evolution of Social Media",
                    "The Art of Cooking"
                ]


        contents = [
                    "Exploring the future of artificial intelligence and its impact on society.As AI continues to advance, it promises to revolutionize industries—from healthcare and education to transportation and finance—by improving efficiency, personalization, and decision-making. However, this progress also raises critical questions about privacy, job displacement, ethical accountability, and the need for robust regulatory frameworks. Striking a balance between innovation and responsibility will be key to ensuring that AI serves the collective good of humanity.",
                    "Discovering solutions to combat climate change and protect the environment. It requires global cooperation, innovative technologies, and sustainable practices across all sectors. From transitioning to renewable energy and preserving biodiversity to reducing carbon emissions and promoting circular economies, every action counts. Empowering communities, enforcing environmental policies, and investing in green innovation are key steps toward a healthier, more resilient planet.",
                    "Analyzing trends and challenges in remote work environments.Analyzing trends in remote work reveals a shift toward flexible, hybrid models driven by digital tools and employee preferences. While it offers increased autonomy and cost savings, challenges like communication gaps, isolation, and maintaining productivity persist. Addressing these requires strong leadership, clear expectations, and a focus on employee well-being and collaboration.",
                    "An introduction to the principles and applications of quantum computing and its potential impact on society.Quantum computing is a revolutionary approach to computation that harnesses the principles of quantum mechanics, such as superposition and entanglement, to process information. Unlike classical computers, which use bits, quantum computers use qubits that can represent multiple states simultaneously. This allows for immense computational power, making quantum computing ideal for solving complex problems in cryptography, drug discovery, optimization, and materials science.",
                    "Investigating the latest innovations in renewable energy sources Advanced energy storage solutions—including flow, solid‑state, iron‑air, and thermal batteries—are scaling to enable 24/7 renewable power and grid resilience.",
                    "Understanding the fundamentals of robotics and their real-world applicationsCore concepts include mechanics, electronics, sensors, control systems, and artificial intelligence. In the real world, robotics is transforming industries such as manufacturing, healthcare, agriculture, and logistics. From surgical robots and automated warehouses to drones and robotic arms, these technologies enhance precision, efficiency, and safety across a wide range of applications..",
                    "Understanding the fundamentals of deep learning and neural networks.artificial neural networks, inspired by the human brain, which consist of layers of interconnected nodes (neurons) that process and transform inputs to predict outcomes. Deep learning refers to networks with many hidden layers, enabling them to learn complex features and relationships. These models power breakthroughs in image recognition, natural language processing, autonomous vehicles, and more—redefining what machines can achieve in data-driven tasks.",
                    "Examining the economic landscape in the aftermath of the COVID-19 pandemic.Examining the economic landscape in the aftermath of the COVID-19 pandemic, we see a shift towards economic resilience and sustainability. Governments and businesses are investing in recovery programs, green technologies, and workforce development. The ",
                    "Exploring the potential of blockchain technology in the financial sector.Exploring the potential of blockchain technology in the financial sector reveals transformative possibilities for transparency, security, and efficiency. By enabling decentralized and tamper-proof record-keeping, blockchain can streamline processes like cross-border payments, trade settlements, and identity verification. It reduces reliance on intermediaries, lowers costs, and increases transaction speed. Applications such as smart contracts and decentralized finance (DeFi) are reshaping how financial services are delivered, offering greater accessibility and control to users. As adoption grows, blockchain holds the promise to redefine the foundations of modern finance.",
                    "Harnessing the power of storytelling to create compelling marketing campaigns.Examining the economic landscape in the aftermath of the COVID-19 pandemic",
                    "Highlighting breakthroughs and advancements in medical technology.Examining the economic landscape in the aftermath of the COVID-19 pandemic",
                    "Addressing the obstacles and opportunities in space exploration.Key obstacles include high costs, radiation exposure, life support sustainability, and propulsion limitations for long-distance travel. However, the opportunities are equally compelling—ranging from advancing scientific knowledge and discovering extraterrestrial life to developing new technologies and potential human settlement on other planets. As public and private efforts expand, space exploration promises to redefine humanity’s future beyond Earth.",
                    "Exploring the psychological factors influencing decision-making processes.Celebrating the art of cooking and culinary creativity means embracing food as both nourishment and a form of expression. It’s about blending flavors, experimenting with ingredients, and honoring cultural traditions while crafting something uniquely personal. From home kitchens to gourmet restaurants, cooking brings people together, tells stories, and sparks joy. Whether it’s a simple meal or an elaborate dish, the creative process behind cooking reflects passion, imagination, and the universal love for good food.",
                    "Tracing the evolution of social media platforms and their impact on society.Examining the economic landscape in the aftermath of the COVID-19 pandemic",
                    "Celebrating the art of cooking and culinary creativity.Celebrating the art of cooking and culinary creativity means embracing food as both nourishment and a form of expression. It’s about blending flavors, experimenting with ingredients, and honoring cultural traditions while crafting something uniquely personal. From home kitchens to gourmet restaurants, cooking brings people together, tells stories, and sparks joy. Whether it’s a simple meal or an elaborate dish, the creative process behind cooking reflects passion, imagination, and the universal love for good food."
                ]

        img_urls = [
                    "https://picsum.photos/id/1/800/400",
                    "https://picsum.photos/id/2/800/400",
                    "https://picsum.photos/id/3/800/400",
                    "https://picsum.photos/id/4/800/400",
                    "https://picsum.photos/id/5/800/400",
                    "https://picsum.photos/id/6/800/400",
                    "https://picsum.photos/id/7/800/400",
                    "https://picsum.photos/id/8/800/400",
                    "https://picsum.photos/id/9/800/400",
                    "https://picsum.photos/id/10/800/400",
                    "https://picsum.photos/id/11/800/400",
                    "https://picsum.photos/id/12/800/400",
                    "https://picsum.photos/id/13/800/400",
                    "https://picsum.photos/id/14/800/400",
                    "https://picsum.photos/id/15/800/400"
                ]

        categories= Category.objects.all()
        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))

