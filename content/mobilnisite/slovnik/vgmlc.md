---
slug: "vgmlc"
url: "/mobilnisite/slovnik/vgmlc/"
type: "slovnik"
title: "VGMLC – Visited Gateway Mobile Location Centre"
date: 2025-01-01
abbr: "VGMLC"
fullName: "Visited Gateway Mobile Location Centre"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vgmlc/"
summary: "VGMLC je GMLC umístěný v navštívené síti, když roamující účastník vyžaduje služby určování polohy. Slouží jako zprostředkovatel k ochraně soukromí účastníka a prosazování místních předpisů, čímž zajiš"
---

VGMLC je Gateway Mobile Location Centre v navštívené síti, který bezpečně získává informace o poloze pro roamujícího účastníka při současné ochraně soukromí a dodržování místních předpisů.

## Popis

Visited Gateway Mobile Location Centre (VGMLC) je entita základní sítě definovaná v 3GPP pro služby založené na poloze ([LBS](/mobilnisite/slovnik/lbs/)), která konkrétně funguje v rámci navštívené veřejné pozemní mobilní sítě ([VPLMN](/mobilnisite/slovnik/vplmn/)), když je mobilní účastník v roamingu. Architektonicky funguje jako typ Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)), který sídlí v síti, kde se účastník aktuálně nachází, na rozdíl od domácího GMLC ([HGMLC](/mobilnisite/slovnik/hgmlc/)) v domovské síti účastníka. VGMLC slouží jako bod pro prosazování ochrany soukromí a regulací, zachycuje požadavky na polohu od externích klientů služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/) klienti) nebo od HGMLC, než dorazí k polohovacím systémům navštívené sítě. Jeho hlavní rolí je ověřovat a autorizovat dotazy na polohu, uplatňovat místní pravidla ochrany soukromí a zajistit soulad s právními požadavky navštívené země na zveřejnění polohy.

Když je pro roamujícího účastníka zahájen požadavek na polohu, HGMLC nejprve identifikuje, že je účastník v navštívené síti, a přepošle požadavek na VGMLC přes standardizovaná rozhraní jako Lg nebo SLh. VGMLC poté provede kontroly ochrany soukromí na základě profilu účastníka a místních předpisů, což může zahrnovat ověření souhlasu, kontrolu nastavení blokování nebo aplikaci dodatečného ověření. Pokud je požadavek autorizován, VGMLC komunikuje s Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) navštívené sítě a se Serving Mobile Location Centre ([SMLC](/mobilnisite/slovnik/smlc/)), aby získal polohu účastníka pomocí metod jako Cell-ID, OTDOA nebo A-GPS. Získaná data o poloze jsou následně formátována a vrácena HGMLC, který je přepošle LCS klientovi, čímž je zajištěno, že citlivé informace o poloze neopustí navštívenou síť bez patřičných kontrol.

Klíčové komponenty související s VGMLC zahrnují HGMLC, který iniciuje požadavky; SMLC, který vypočítává odhady polohy; a MSC/MME, který poskytuje kontext účastníka. VGMLC implementuje rozhraní jako Lg pro okruhově spínané domény a SLh pro IP domény, v souladu s vyvíjející se architekturou 3GPP. Podporuje různé typy služeb LCS, včetně nouzových, přidané hodnoty a služeb zákonného odposlechu, s přizpůsobenými postupy pro každý typ. Tím, že VGMLC funguje jako strážce, zabraňuje neoprávněnému sledování polohy, snižuje bezpečnostní rizika a zajišťuje, že s daty o poloze roamujících účastníků je nakládáno v souladu s politikami domácí i navštívené sítě, což usnadňuje služby LBS přes hranice při zachování důvěry a souladu s předpisy.

## K čemu slouží

VGMLC byl zaveden k řešení výzev v oblasti ochrany soukromí, bezpečnosti a regulace při poskytování služeb založených na poloze roamujícím účastníkům napříč různými síťovými operátory a zeměmi. Před jeho standardizací byly požadavky na polohu pro roamující uživatele často zpracovávány přímo GMLC domácí sítě, což mohlo obcházet místní zákony na ochranu soukromí a předpisy navštívené země. To představovalo právní rizika, protože země mají různé požadavky na zveřejňování údajů o poloze, například pro nouzové služby nebo zákonný odposlech. VGMLC to řeší tím, že zajišťuje, aby k získávání polohy docházelo v jurisdikci navštívené sítě, kde lze uplatňovat místní pravidla, čímž chrání jak účastníky, tak operátory před porušením předpisů.

Motivace vychází z rostoucí poptávky po službách LBS, jako je nouzové volání (např. E911 v USA), navigace a sledování vozového parku, které vyžadují přesnou polohu i při mezinárodním roamingu. Bez VGMLC by navštívené sítě mohly postrádat kontrolu nad dotazy na polohu, což by vedlo k potenciálnímu zneužití nebo neoprávněnému přístupu. Nasazením VGMLC mohou navštívení operátoři implementovat vlastní politiky ochrany soukromí, ověřovat externí požadavky a zaznamenávat transakce s polohou pro audit, čímž zvyšují bezpečnost. To je zvláště kritické pro nouzové služby, kde musí být poloha poskytnuta rychle a přesně místním orgánům bez ohledu na domovskou síť účastníka.

Historicky se VGMLC objevil ve 3GPP Release 16 jako součást širších vylepšení architektury LCS, což odráží zvýšený důraz na předpisy na ochranu soukromí, jako je GDPR. Řeší omezení dřívějších přístupů, kdy HGMLC přímo přistupoval k prvkům navštívené sítě, což mohlo ohrozit soukromí účastníka a soulad s předpisy. Zavedením VGMLC umožnila 3GPP bezproblémové a bezpečné služby LBS přes hranice, podporující globální roaming a zároveň zajišťující, že zpracování dat o poloze odpovídá místním právním rámcům, čímž podporuje důvěru a interoperabilitu v mobilních sítích.

## Klíčové vlastnosti

- Slouží jako bod prosazování ochrany soukromí v navštívené síti pro služby určování polohy roamujících účastníků
- Ověřuje a autorizuje požadavky na polohu z domácí sítě nebo od externích klientů
- Aplikuje místní regulační a ochranářské politiky před zveřejněním informací o poloze
- Komunikuje s SMLC a MSC/MME navštívené sítě pro získání polohovacích dat
- Podporuje typy služeb určování polohy: nouzové, komerční a pro zákonný odposlech
- Zajišťuje soulad s předpisy na ochranu dat přes hranice, jako je GDPR

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [HGMLC – Home Gateway Mobile Location Centre](/mobilnisite/slovnik/hgmlc/)
- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)

## Definující specifikace

- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 33.814** (Rel-16) — Security aspects of enhanced Location Services (eLCS)

---

📖 **Anglický originál a plná specifikace:** [VGMLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/vgmlc/)
