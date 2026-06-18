---
slug: "rrp"
url: "/mobilnisite/slovnik/rrp/"
type: "slovnik"
title: "RRP – MIPv4 Registration Response"
date: 2025-01-01
abbr: "RRP"
fullName: "MIPv4 Registration Response"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rrp/"
summary: "MIPv4 Registration Response (RRP) je protokolová zpráva vysílaná domácím agentem (Home Agent, HA) jako odpověď na registrační žádost (Registration Request, RRQ) od mobilního uzlu (Mobile Node, MN) v M"
---

RRP je zpráva odpovědi na registraci v Mobile IPv4 (MIPv4 Registration Response), kterou vysílá domácí agent (Home Agent), aby potvrdil nebo zamítl žádost mobilního uzlu (Mobile Node) o registraci jeho přechodné adresy (care-of address), čímž umožňuje IP mobilitu a kontinuitu relace.

## Popis

MIPv4 Registration Response (RRP) je klíčová zpráva řídicí roviny v protokolu Mobile IPv4 (MIPv4), standardizovaná [IETF](/mobilnisite/slovnik/ietf/) a přijatá 3GPP pro určité funkce správy IP mobility. Generuje ji a vysílá domácí agent (Home Agent, [HA](/mobilnisite/slovnik/ha/)) mobilního uzlu po přijetí registrační žádosti (Registration Request, [RRQ](/mobilnisite/slovnik/rrq/)) od tohoto uzlu. RRP putuje sítí zpět k [MN](/mobilnisite/slovnik/mn/), typicky přes cizího agenta (Foreign Agent, [FA](/mobilnisite/slovnik/fa/)), pokud je využit, aby doručila rozhodnutí HA ohledně pokusu o registraci.

Struktura paketu RRP je definována protokolem MIPv4 ([RFC](/mobilnisite/slovnik/rfc/) 5944). Obsahuje několik klíčových polí: pole Type identifikující zprávu jako odpověď na registraci; pole Code udávající úspěch nebo konkrétní důvod selhání (např. úspěšná registrace, selhání autentizace, příliš dlouhá životnost); pole Home Address a Home Agent identifikující MN a jeho HA; pole Identification odpovídající hodnotě v příslušné RRQ, aby se zabránilo opakovaným útokům; a udělenou životnost (Lifetime) pro vazbu. Pokud je registrace úspěšná, tato vazba uloží asociaci mezi stálou domácí adresou MN a jeho dočasnou přechodnou adresou (Care-of Address, CoA) do vyrovnávací paměti vazeb (binding cache) HA.

Primární funkcí RRP je informovat MN o výsledku jeho registračního pokusu. Úspěšná RRP (Code 0) autorizuje MN k použití registrované CoA. HA následně začne zachytávat pakety určené pro domácí adresu MN, zapouzdřovat je a tunelovat je na CoA. Zamítnutá RRP (nenulový Code) nutí MN k nápravným krokům, jako je opětovná autentizace, nalezení nového FA nebo úprava požadovaných parametrů. RRP tak finalizuje tříkrokový registrační proces (RRQ -> RRP -> případně RRQ/potvrzení) a zakládá tunel nezbytný pro transparentní mobilitu.

V rámci architektur 3GPP byly MIPv4 a tedy i zpráva RRP specifikovány primárně pro mobilitu mezi systémy a rané služby založené na IP, zejména v kontextu propojení s bezdrátovou lokální sítí ([WLAN](/mobilnisite/slovnik/wlan/)) definovaném v raných vydáních. RRP jako součást signalizace MIPv4 umožňuje uživatelskému zařízení (UE) zachovat kontinuitu IP relace při pohybu mezi 3GPP a ne-3GPP přístupovými sítěmi (jako je WLAN) tím, že registruje svůj bod připojení u HA v jádru 3GPP.

## K čemu slouží

MIPv4 Registration Response funguje jako autoritativní odpověď v signalizačním protokolu Mobile IPv4, který byl vytvořen k řešení problému udržování probíhající IP komunikace pro zařízení měnící svůj bod připojení k síti. Bez takového protokolu by se IP adresa mobilního hostitele při přesunu do nové sítě změnila a přerušila všechny existující TCP spojení a [UDP](/mobilnisite/slovnik/udp/) relace. MIPv4, a tím i RRP, umožňuje 'nomádskou' mobilitu na IP vrstvě.

Historicky byl MIPv4 vyvinut IETF jako řešení mobility založené na hostiteli ještě předtím, než 3GPP vyvinulo své vlastní síťové protokoly mobility, jako je GPRS Tunneling Protocol (GTP). 3GPP začlenilo MIPv4 ve vydáních jako Rel-8, aby poskytlo standardizovanou metodu pro mobilitu mezi 3GPP sítěmi a jinými IP přístupovými sítěmi, nejvýznamněji WLAN. RRP plní kritický účel poskytnutí bezpečného a autentizovaného potvrzení od sítě (domácího agenta), že nová poloha mobilního uzlu byla oficiálně zaznamenána, čímž uzavírá registrační proces.

RRP řeší omezení jednoduchého mechanismu žádosti bez odpovědi tím, že poskytuje nezbytnou zpětnou vazbu. Přenáší nejen úspěch/selhání, ale i specifické kódy chyb, které umožňují mobilnímu uzlu diagnostikovat problémy (např. nedostatečná autentizace, chybně vytvořená žádost, zamítnuto administrátorem). Rovněž oficiálně sděluje životnost vazby (binding lifetime) udělenou HA, která se může lišit od požadované životnosti, což HA umožňuje kontrolovat využití zdrojů. Tento řízený mechanismus odpovědi je zásadní pro bezpečnou a spravovatelnou IP mobilitu, neboť zajišťuje, že pouze autorizované uzly mohou přesměrovávat provoz a že síťové zdroje jsou přidělovány a časovány správně.

## Klíčové vlastnosti

- Finalizuje registrační proceduru MIPv4 tím, že poskytne rozhodnutí domácího agenta
- Obsahuje výsledkový kód (result code) udávající úspěch nebo konkrétní důvod selhání
- Sděluje oficiálně udělenou životnost vazby (binding lifetime) pro relaci mobility
- Obsahuje odpovídající identifikační pole (identification field) pro spárování s příslušnou registrační žádostí
- Autentizuje odpověď, aby se zabránilo podvržení a zajistila integrita
- Při úspěchu aktivuje domácího agenta k vytvoření tunelu pro přeposílání provozu

## Související pojmy

- [RRQ – MIPv4 Registration Request](/mobilnisite/slovnik/rrq/)
- [PMIP – Proxy Mobile Internet Protocol version 6](/mobilnisite/slovnik/pmip/)

## Definující specifikace

- **TS 24.304** (Rel-19) — MIPv4 FA Mode Mobility Management in EPC
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.279** (Rel-19) — MIPv4 Mobility Protocol over S2a
- **TS 33.822** (Rel-8) — Security Architecture for Inter-Access Mobility

---

📖 **Anglický originál a plná specifikace:** [RRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rrp/)
