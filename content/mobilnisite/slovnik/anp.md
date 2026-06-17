---
slug: "anp"
url: "/mobilnisite/slovnik/anp/"
type: "slovnik"
title: "ANP – Access Network Provider"
date: 2025-01-01
abbr: "ANP"
fullName: "Access Network Provider"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/anp/"
summary: "Poskytovatel přístupové sítě (ANP) je subjekt odpovědný za provoz infrastruktury rádiové přístupové sítě (RAN), včetně základnových stanic a rádiových řadičů. Zajišťuje fyzické připojení uživatelského"
---

ANP je subjekt odpovědný za provoz infrastruktury rádiové přístupové sítě, který zajišťuje fyzické připojení uživatelského zařízení ke službám jádrové sítě.

## Popis

Poskytovatel přístupové sítě (ANP) je logický a administrativní subjekt v rámci systémové architektury 3GPP, který je oddělený od poskytovatele jádrové sítě (CNP) a poskytovatele služeb (SP). Jeho hlavní funkcí je vlastnit, spravovat a provozovat infrastrukturu rádiové přístupové sítě (RAN). Tato infrastruktura zahrnuje všechny fyzické a logické komponenty nezbytné pro navázání rádiového spojení s uživatelským zařízením (UE), včetně Node B (v UMTS), eNodeB (v LTE), gNB (v 5G NR) a jejich přidružených řadičů, jako je Radio Network Controller (RNC) nebo Central Units ([CU](/mobilnisite/slovnik/cu/)). ANP je odpovědný za správu rádiových zdrojů, provádění předávání hovorů (handover) a přenos dat uživatelské a řídicí roviny mezi UE a okrajem jádrové sítě.

Z architektonického hlediska ANP provozuje síťový segment definovaný rozhraním Uu (mezi UE a přístupovým uzlem) a typicky rozhraním Iu (pro UMTS) nebo [NG](/mobilnisite/slovnik/ng/) (pro 5G) směrem k jádrové síti. Nevlastní data účastníků ani neposkytuje koncovým uživatelům služby jako hlasové hovory nebo internetové balíčky; to je doména poskytovatele služeb. Místo toho ANP poskytuje konektivitu typu 'bit pipe' (přenosový kanál) a nabízí hromadné přístupové služby jednomu nebo více CNP/SP. Jeho provozní povinnosti zahrnují plánování rádiové sítě, nasazení, údržbu, optimalizaci lokalit buněk a zajišťování kvality a pokrytí rádiového signálu.

Role ANP je zvláště významná ve scénářích s více operátory nebo při využití neutrálního hostitele. Například v rámci dohod o sdílení sítě, jako je Multi-Operator Core Network ([MOCN](/mobilnisite/slovnik/mocn/)) nebo Gateway Core Network ([GWCN](/mobilnisite/slovnik/gwcn/)), jeden ANP (což může být jeden operátor nebo společnost třetí strany vlastnící infrastrukturu) poskytuje přístup k RAN více operátorům jádrových sítí. Toto oddělení umožňuje efektivnější využití spektra a infrastruktury, snižuje náklady na nasazení a může urychlit rozšíření síťového pokrytí. Výkon ANP přímo ovlivňuje klíčové metriky uživatelského zážitku, jako je propustnost dat, latence a míra ztráty hovorů, protože spravuje inherentně omezené a proměnlivé rádiové zdroje.

Z obchodního a standardizačního hlediska definice ANP objasňuje odpovědnosti, rozhraní a fakturační vztahy v disagregovaném telekomunikačním ekosystému. Specifikace 3GPP, zejména ty zabývající se síťovou architekturou a správou (jako TS 37.808), definují funkční požadavky a rozhraní, která musí ANP podporovat pro interoperabilitu s jádrovými sítěmi různých poskytovatelů. Toto jasné vymezení podporuje regulační rámce, umožňuje konkurenci a usnadňuje inovace, jako jsou mobilní virtuální síťoví operátoři ([MVNO](/mobilnisite/slovnik/mvno/)), kteří nemusí vlastnit žádnou přístupovou síť, ale pro konektivitu se zcela spoléhají na ANP.

## K čemu slouží

Koncept poskytovatele přístupové sítě byl formálně zaveden, aby řešil vývojové obchodní a architektonické modely v telekomunikačním průmyslu, zejména oddělení vlastnictví sítě od poskytování služeb. Před touto formalizací byl typickým modelem vertikálně integrovaný operátor, který vlastnil jak RAN, tak jádrovou síť a přímo poskytoval služby koncovým uživatelům. Tento model omezoval flexibilitu, činil vstup na trh pro nové poskytovatele služeb nákladným (protože potřebovali vybudovat celou síť) a mohl vést k neefektivní duplikaci infrastruktury, zejména ve venkovských oblastech.

Model ANP byl motivován potřebou umožnit konkurenci, sdílení infrastruktury a snížit kapitálové ([CAPEX](/mobilnisite/slovnik/capex/)) a provozní ([OPEX](/mobilnisite/slovnik/opex/)) výdaje. Definováním jasného subjektu odpovědného výhradně za přístupovou vrstvu standardy 3GPP podpořily vznik poskytovatelů v roli neutrálního hostitele a dohod o sdílení sítě. To umožňuje například společnosti vybudovat a provozovat hustou síť malých buněk na stadionu nebo na letišti a prodávat přístupovou kapacitu více mobilním síťovým operátorům ([MNO](/mobilnisite/slovnik/mno/)), z nichž žádný by nemohl ekonomicky odůvodnit nasazení vlastní infrastruktury v dané lokalitě.

Toto oddělení je navíc základním principem pro pokročilé architektonické koncepty, jako je dělení sítě (network slicing) a Open RAN (O-RAN). Umožňuje abstrakci a rozdělení zdrojů RAN (spravovaných ANP) za účelem vytvoření virtualizovaných, end-to-end síťových řezů šitých na míru různým poskytovatelům služeb nebo případům užití (např. řez pro službu automatizace továrny spravovaný jedním SP a řez pro veřejný širokopásmový přístup spravovaný jiným). Koncept ANP tedy činí architekturu připravenou na budoucnost a umožňuje dynamičtější, efektivnější a různorodější obchodní ekosystémy přesahující tradiční model monolitického operátora.

## Klíčové vlastnosti

- Vlastní a provozuje fyzickou infrastrukturu RAN (základnové stanice, antény, přenosové trasy fronthaul/backhaul)
- Spravuje přidělování rádiových zdrojů, správu mobility (předávání hovorů) a zřizování/ukončování spojení
- Poskytuje standardizovaná rozhraní (např. Iu, NG) pro propojení s jedním nebo více poskytovateli jádrové sítě
- Umožňuje modely sdílení sítě, jako jsou MOCN a GWCN, pro lepší využití infrastruktury
- Podporuje scénáře s neutrálním hostitelem, umožňující poskytovatelům infrastruktury třetích stran službu více operátorům
- Usnadňuje jasné provozní a obchodní vymezení mezi přístupovou, jádrovou a služební vrstvou

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 37.808** (Rel-12) — PIM Handling for Base Stations Study

---

📖 **Anglický originál a plná specifikace:** [ANP na 3GPP Explorer](https://3gpp-explorer.com/glossary/anp/)
