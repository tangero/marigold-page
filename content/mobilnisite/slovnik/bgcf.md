---
slug: "bgcf"
url: "/mobilnisite/slovnik/bgcf/"
type: "slovnik"
title: "BGCF – Breakout Gateway Control Function"
date: 2026-01-01
abbr: "BGCF"
fullName: "Breakout Gateway Control Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bgcf/"
summary: "BGCF je funkcí řízení komunikačních relací v IMS, která vybírá vhodnou síť pro směrování SIP relací do PSTN nebo do okruhově spínané domény. Rozhoduje, zda má k breakoutu dojít ve stejné síti nebo v s"
---

BGCF je funkcí řízení komunikačních relací v IMS, která vybírá síť pro směrování SIP relací do PSTN nebo do okruhově spínané domény a volí příslušný bod breakoutu, například MGCF.

## Popis

Breakout Gateway Control Function (BGCF) je klíčovou komponentou architektury IP Multimedia Subsystem (IMS), konkrétně v rámci vrstvy Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)). Její hlavní rolí je činit rozhodnutí o směrování pro SIP relace, které je třeba ukončit v okruhově spínané síti ([CS](/mobilnisite/slovnik/cs/)), jako je Public Switched Telephone Network (PSTN) nebo starší mobilní síť (např. 2G/3G). Když je SIP relace iniciovaná v rámci IMS určena pro uživatele nebo službu v CS doméně, Serving-CSCF (S-CSCF) přepošle signalizaci relace na BGCF. BGCF pak analyzuje požadavek na relaci, typicky na základě volaného čísla (E.164), aby rozhodl, kde má relace 'opustit' (breakout) paketové jádro IMS a vstoupit do CS domény.

Z architektonického hlediska je BGCF SIP server implementující specifickou směrovací logiku. Nezprostředkovává přenos médií, činí čistě signalizační rozhodnutí. Po přijetí SIP INVITE požadavku BGCF vyhodnotí cíl. Pokud je rozhodnuto, že bod breakoutu se nachází v jeho vlastní síti, BGCF vybere vhodnou Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) ve své doméně a přepošle jí SIP signalizaci. MGCF je pak zodpovědná za vzájemné propojení SIP signalizace se signalizací [ISUP](/mobilnisite/slovnik/isup/)/BICC používanou v CS síti a za řízení Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) pro konverzi médií. Pokud má být breakout zpracován lépe v jiné síti, úlohou BGCF je vybrat partnerský BGCF v této externí síti a přeposlat mu SIP relaci, čímž deleguje finální rozhodnutí o breakoutu.

Klíčové součásti funkcionality BGCF zahrnují její databázi směrovací logiky a její rozhraní. Rozhraní se S-CSCF je realizováno přes referenční bod Mr (pomocí SIP) a s dalšími BGCF přes referenční bod Mi (také SIP). Její vnitřní rozhodování může být založeno na konfigurovaných směrovacích tabulkách, analýze čísel, politikách operátora nebo interakcích s dalšími síťovými elementy, jako je Transport Stratum pro [ENUM](/mobilnisite/slovnik/enum/)/[DNS](/mobilnisite/slovnik/dns/) dotazy k překladu telefonních čísel na SIP URI nebo směrovací čísla. Výběrový proces BGCF zajišťuje optimální směrování, distribuci zátěže mezi MGCF a dodržování komerčních dohod mezi síťovými operátory pro mezisíťový breakout.

V širší IMS architektuře je role BGCF klíčová pro bezproblémovou kontinuitu služeb. Umožňuje IMS, což je plně IP platforma pro poskytování služeb, připojit se k rozsáhlé instalované základně uživatelů a služeb starší telefonie. Bez BGCF by volání iniciovaná z IMS nemohla dosáhnout čísel v PSTN, což by vážně omezilo její užitečnost. Její činnost je pro koncového uživatele transparentní, ale je základním prvkem umožňujícím vizi 'konvergence pevných a mobilních sítí' (fixed-mobile convergence) v IMS, což poskytovatelům služeb umožňuje nabízet jednotné komunikační služby přes hranice paketově a okruhově spínaných domén.

## K čemu slouží

BGCF byla vytvořena k řešení zásadního problému při přechodu z okruhově spínaných na paketově spínané telefonní sítě. Když 3GPP definovala IMS ve verzi Release 5 pro poskytování multimediálních služeb přes IP, byl potřebný mechanismus pro propojení této nové signalizační IP domény (SIP) s existující globální PSTN a staršími mobilními [CS](/mobilnisite/slovnik/cs/) jádry, které používaly signalizační protokoly jako ISUP. Primárním problémem bylo určit *kde* a *jak* provést toto protokolové propojení a konverzi médií škálovatelným, efektivním a politicky řízeným způsobem.

Historicky, v čistě CS sítích, byla volání směrována přes přepínače na základě hierarchických číselných plánů. V IMS je směrování založeno na SIP URI a IP adresách. BGCF poskytuje inteligenci potřebnou k propojení těchto dvou světů. Řeší omezení spočívající v jediném, pevném bodu breakoutu, který by mohl vytvářet úzká místa nebo suboptimální směrování (např. 'trombónování' hovorů zpět do domovské sítě). Díky dynamickému výběru umožňuje BGCF provést breakout blíže k cíli, čímž snižuje latenci a náklady na přenos. Umožňuje také síťovým operátorům implementovat sofistikované směrovací politiky, jako je výběr bodu breakoutu na základě denní doby, nejlevnějšího směrování nebo scénářů převzetí služeb při selhání.

Dále BGCF podporuje dekompozici síťových funkcí, kterou IMS prosazuje. Oddělení rozhodnutí o směrování (BGCF) od protokolového propojení a řízení médií (MGCF) umožňuje nezávislé škálování a vývoj těchto funkcí. Tato modularita byla klíčovou motivací v návrhu IMS, poskytující flexibilitu síťovým operátorům pro efektivní nasazení a správu zdrojů. BGCF tedy existuje nejen jako brána, ale jako strategický směrovací uzel, který umožňuje ekonomickou a technickou proveditelnost nasazení IMS vedle – a nakonec jako náhrady za – starší telefonní infrastrukturu.

## Klíčové vlastnosti

- Vybírá síť a uzel pro breakout relací z IMS do CS/PSTN
- Činí rozhodnutí o směrování na základě analýzy cílového čísla a politiky operátora
- Přeposílá relace na MGCF ve stejné síti nebo na partnerský BGCF v jiné síti
- Komunikuje s S-CSCF (Mr) a dalšími BGCF (Mi) pomocí SIP
- Umožňuje optimální směrování za účelem snížení latence a nákladů na propojení
- Podporuje distribuci zátěže a redundanci mezi více MGCF

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 23.815** (Rel-5) — IMS Charging Implications
- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.429** (Rel-7) — Explicit Communication Transfer (ECT) Service Specification
- **TS 24.454** (Rel-8) — Closed User Group (CUG) Protocol Specification
- **TS 24.508** (Rel-8) — TIP and TIR Service Protocol Description
- **TS 24.516** (Rel-8) — MCID Protocol Specification for NGN
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 24.529** (Rel-8) — Explicit Communication Transfer (ECT) Simulation Service
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [BGCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/bgcf/)
