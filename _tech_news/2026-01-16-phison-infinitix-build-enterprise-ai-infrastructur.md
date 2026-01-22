---
author: Marisa Aigen
category: ai infrastruktura
companies:
- Phison
- Infinitix
date: '2026-01-16 07:12:33'
description: Phison spolupracuje s poskytovatelem softwaru Infinitix na integraci
  své technologie aiDAPTIV+ s platformou AI-Stack. Řešení sjednocuje hardware a software
  pro trénink a inference AI modelů v podnikovém prostředí s využitím vysokorychlostních
  SSD a expanze paměti.
importance: 4
layout: tech_news_article
original_title: Phison, Infinitix build enterprise AI infrastructure stack
publishedAt: '2026-01-16T07:12:33+00:00'
slug: phison-infinitix-build-enterprise-ai-infrastructur
source:
  emoji: 📰
  id: null
  name: Digitimes
title: Phison a Infinitix budují infrastrukturní stack pro podnikové AI
url: https://www.digitimes.com/news/a20260116PD234/phison-hardware-ai-infrastructure-training.html
urlToImage: https://img.digitimes.com/newsshow/20260116pd234_files/1_b.jpg
urlToImageBackup: https://img.digitimes.com/newsshow/20260116pd234_files/1_b.jpg
---

## Souhrn
Phison, taiwanský výrobce úložišť a SSD, navázal partnerství s Infinitix, firmou zaměřenou na software pro správu AI infrastruktury. Společně integrují technologii aiDAPTIV+ s platformou AI-Stack, čímž vytvářejí ucelené řešení pro podnikové AI trénink a inference. Tento stack překonává limity tradičních pamětí HBM a GDDR pomocí vysokorychlostních SSD a inteligentní expanze paměti v prostředí Kubernetes.

## Klíčové body
- Integrace Phison aiDAPTIV+ s Infinitix AI-Stack pro sjednocení hardware a software v AI infrastruktuře.
- Využití NAND úložišť jako expanze paměti k překonání omezení HBM a GDDR.
- Podpora plánování AI úloh v Kubernetes s hardware akcelerací.
- Flexibilní škálování pro velké datové centra s heterogenními zdroji (výpočet, paměť, úložiště).
- Zaměření na efektivitu a snížení nákladů oproti tradičním AI architekturám.

## Podrobnosti
Phison, globální lídr v produkci SSD a řídicích čipů pro úložiště, představil technologii aiDAPTIV+, která umožňuje dynamickou adaptaci NAND flash úložišť pro AI aplikace. Tato technologie funguje jako inteligentní vrstva expanze paměti, kde SSD přebírají roli rychlé mezipaměti nebo dokonce náhrady za drahé HBM (High Bandwidth Memory) a GDDR paměti, které jsou v současných AI systémech limitující kvůli vysoké ceně a omezené kapacitě. Infinitix, startup specializující se na software pro orchestraci AI infrastruktury, vyvinul platformu AI-Stack, která slouží k plánování a správě AI úloh v nativním Kubernetes prostředí. Tato platforma umožňuje automatizované rozdělování zdrojů mezi GPU, paměti a úložišti, což zrychluje trénink velkých modelů a jejich nasazení pro inference.

Partnerství kombinuje tyto prvky do end-to-end řešení: aiDAPTIV+ poskytuje hardware akceleraci na úrovni úložiště, zatímco AI-Stack zajišťuje softwarovou koordinaci. Výsledek je podnikové AI platformy schopné zpracovávat velké modely na více uzlech bez nutnosti masivních investic do HBM. Například v datových centrech lze nyní integrovat heterogenní hardware – od NVIDIA GPU po Phison SSD – do jedné škálovatelné architektury. Podle CEO Infinitix WenYu Chena se AI posouvá od hrubé výpočetní síly k efektivnímu managementu zdrojů, což tento stack přímo podporuje. Phison CEO KS Pua zdůrazňuje přechod od jednogpu systémů k distribuovaným architekturám, kde NAND úložiště hraje klíčovou roli v škálování.

Toto řešení je navrženo pro Kubernetes-native prostředí, což znamená kompatibilitu s otevřenými nástroji jako Kubernetes orchestrátor, který slouží k nasazení kontejnerizovaných aplikací. Firmy tak mohou trénovat modely jako Llama nebo GPT varianty na clusteru s optimalizovaným výkonem, aniž by čelily bottleneckům v paměti.

## Proč je to důležité
V éře rostoucí poptávky po AI compute, kde trénink velkých modelů vyžaduje terabajty paměti, tradiční HBM a GDDR brání škálování kvůli ceně a dostupnosti. Toto partnerství přináší storage-layer optimalizaci přímo do AI plánovače, což umožňuje podnikům budovat nákladově efektivní datová centra. Pro průmysl znamená snížení závislosti na proprietárních GPU pamětích a podporu otevřených standardů jako Kubernetes, což urychluje adopci AI v enterprise. V širším kontextu posiluje roli NAND úložišť v AI ekosystému, kde Phison konkuruje hráčům jako Samsung nebo Micron, a pomáhá řešit energetickou náročnost AI tréninku. Očekává se, že takové stacky budou klíčové pro nasazení AI na hranici cloudu a edge, kde je flexibilita rozhodující.

---

[Číst původní článek](https://www.digitimes.com/news/a20260116PD234/phison-hardware-ai-infrastructure-training.html)

**Zdroj:** 📰 Digitimes
