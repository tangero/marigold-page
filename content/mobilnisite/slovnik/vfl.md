---
slug: "vfl"
url: "/mobilnisite/slovnik/vfl/"
type: "slovnik"
title: "VFL – Vertical Federated Learning"
date: 2026-01-01
abbr: "VFL"
fullName: "Vertical Federated Learning"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vfl/"
summary: "Framework distribuovaného strojového učení šetrný k ochraně soukromí, ve kterém více stran společně trénuje model s využitím různých sad příznaků od stejné skupiny uživatelů. Umožňuje spolupráci na da"
---

VFL je framework distribuovaného strojového učení šetrný k ochraně soukromí, ve kterém více stran společně trénuje model s využitím různých sad příznaků od stejné skupiny uživatelů, aniž by odhalovaly nezpracovaná data.

## Popis

Vertikální federované učení (VFL) je specializovaný paradigma distribuovaného strojového učení standardizovaný 3GPP, který umožňuje kolaborativní trénink [AI](/mobilnisite/slovnik/ai/) modelů napříč různými organizacemi nebo síťovými doménami bez centralizace nezpracovaných, citlivých dat. Na rozdíl od horizontálního federovaného učení, kde účastníci sdílejí stejný příznakový prostor, ale různé vzorky uživatelů, se VFL vyznačuje tím, že účastníci mají různé příznaky nebo atributy pro stejnou sadu překrývajících se uživatelských identifikátorů. Typický scénář zahrnuje mobilního operátora, který vlastní data měření rádiové přístupové sítě (RAN), a poskytovatele [OTT](/mobilnisite/slovnik/ott/) služeb, který vlastní data kvality na aplikační vrstvě pro stejné účastníky. VFL umožňuje těmto stranám společně trénovat komplexnější a přesnější model – například pro predikci uživatelského zážitku – zatímco si každá strana udržuje svou vlastní datovou sadu v soukromí a na svých vlastních systémech.

Technický provoz VFL zahrnuje strukturovaný protokol s rolemi, jako je hostující strana, hostitelská strana(y) a případně koordinátor. Proces začíná zarovnáním entit šetrným k ochraně soukromí, kdy účastnící se strany používají kryptografické techniky, jako je Private Set Intersection ([PSI](/mobilnisite/slovnik/psi/)), k bezpečné identifikaci společných uživatelů bez odhalení nepřekrývajících se identifikátorů. Jakmile je vytvořena zarovnaná sada uživatelů, začne kolaborativní trénink. Běžná architektura rozděluje model na spodní model a vrchní model. Každá strana trénuje svůj vlastní spodní model na své lokální sadě příznaků. Výstupy (embeddingy nebo mezivýsledky) z těchto spodních modelů jsou následně bezpečně agregovány, často pomocí homomorfní šifry nebo secure multi-party computation ([MPC](/mobilnisite/slovnik/mpc/)), pro výpočet ztráty a gradientů pro vrchní model. Tyto gradienty jsou distribuovány zpět každé straně pro aktualizaci jejich příslušných spodních modelů, a to vše bez toho, aby jakákoliv strana viděla nezpracované příznaky nebo štítky jiné strany.

Klíčovými součástmi ve frameworku VFL podle 3GPP jsou Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)), která může fungovat jako účastník nebo koordinátor, standardizovaná rozhraní pro orchestraci federovaného učení (např. Naf_FederatedLearning) a bezpečnostní protokoly pro bezpečnou agregaci a výměnu modelů. Architektura je navržena pro integraci s architekturou založenou na službách ([SBA](/mobilnisite/slovnik/sba/)) 5G, což umožňuje síťovým funkcím, jako jsou [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/) a PCF, přispívat daty do procesů federovaného učení. Úlohou VFL je odemknout hodnotu rozdělených datových úložišť v rámci telekomunikačního ekosystému, což umožňuje pokročilé případy užití AI/ML, jako je společné optimalizace sítě a služeb, predikce odchodu zákazníků a personalizovaná správa QoS, při striktním dodržování předpisů na ochranu dat, jako je GDPR.

## K čemu slouží

VFL bylo zavedeno k řešení kritické výzvy datových úložišť a omezení soukromí, která brání rozvoji pokročilého řízení sítí a služeb řízeného AI. V telekomunikačním průmyslu jsou cenná data fragmentována mezi operátory, dodavatele a poskytovatele služeb. Například operátor má detailní data o výkonu sítě, zatímco poskytovatel obsahu má bohatá data o chování aplikací. Tyto datové sady samostatně poskytují omezený pohled; v kombinaci by mohly pohánět vysoce přesné prediktivní modely. Právní, regulační a konkurenční bariéry však brání sdílení nebo centralizaci těchto nezpracovaných dat. Tradiční metody sdružování dat nebo tréninku modelů na centralizovaných datových sadách jsou tedy neproveditelné, což omezuje potenciál AI v 5G a dalších sítích.

Standardizace VFL v 3GPP Release 19 byla motivována potřebou podpořit důvěryhodný ekosystém datové spolupráce pro přípravu na 6G a pokročilé sítě 5G-Advanced. Řeší tento problém poskytnutím standardizovaného, bezpečného frameworku pro kolaborativní učení, který zachovává suverenitu nad daty. To umožňuje účastníkům těžit ze sdružené prediktivní síly distribuovaných sad příznaků a zároveň poskytuje technické a procesní záruky, že nezpracovaná data nikdy neopustí kontrolu jejich vlastníka. VFL odemyká nové obchodní modely a provozní efektivitu, jako je společný vývoj modelů pro predikci odchodu zákazníků s bankovními partnery nebo společné optimalizace streamování videa s obsahovými sítěmi pro doručování, a to vše v rámci frameworku privacy-by-design, který buduje důvěru mezi zainteresovanými stranami.

## Klíčové vlastnosti

- Zarovnání entit šetrné k ochraně soukromí s využitím technik jako Private Set Intersection (PSI)
- Architektura s rozděleným modelem s lokálními spodními modely a společně trénovaným vrchním modelem
- Bezpečný výpočet gradientů a ztráty s využitím homomorfní šifry nebo secure multi-party computation
- Integrace s architekturou založenou na službách (SBA) 5G a NWDAF pro případy užití síťové analytiky
- Standardizovaná rozhraní a procedury pro orchestraci federovaného učení a správu životního cyklu
- Podpora pro heterogenní vlastníky dat s vertikálně rozdělenými příznakovými prostory

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.288** (Rel-20) — 5GS Architecture Enhancements for Data Analytics
- **TS 23.482** (Rel-20) — AIML Enablement Service Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.560** (Rel-19) — AIML Enablement (AIMLE) Services Stage 3 Protocol
- **TS 28.105** (Rel-19) — AI/ML Management for 5GS
- **TS 28.858** (Rel-19) — AI/ML Management Phase 2 Study
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.530** (Rel-19) — AF AI/ML Services Stage 3 Protocol
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- **TS 29.591** (Rel-19) — 5G NEF Southbound Services Stage 3
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.784** (Rel-19) — Security aspects of AI/ML in core network

---

📖 **Anglický originál a plná specifikace:** [VFL na 3GPP Explorer](https://3gpp-explorer.com/glossary/vfl/)
