---
slug: "h-smf"
url: "/mobilnisite/slovnik/h-smf/"
type: "slovnik"
title: "H-SMF – Home Session Management Function"
date: 2025-01-01
abbr: "H-SMF"
fullName: "Home Session Management Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/h-smf/"
summary: "Funkce správy relací (Session Management Function) umístěná v domovské veřejné pozemní mobilní síti (HPLMN) uživatele. Je zodpovědná za správu PDU relací (PDU Sessions) pro roamující koncová zařízení"
---

H-SMF je funkce správy relací (Session Management Function) v domovské síti uživatele, která spravuje PDU relace (PDU Sessions) pro roamující účastníky, pokud není použit Local Breakout, a zajišťuje tak kontrolu domovské sítě nad zásadami relace, účtováním a interakcí s datovou sítí.

## Popis

Home Session Management Function (H-SMF) je funkcí páteřní sítě v rámci architektury 5G systému (5GS), definovanou od 3GPP Release 16 jako součást vylepšených rámců pro roaming a edge computing. Jedná se o konkrétní instanci funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)), která je zodpovědná za správu relace (zřízení, modifikaci, uvolnění), přidělování IP adres, řízení QoS a sběr účtovacích dat. Označení 'Home' (domovská) znamená, že tato SMF sídlí v domovské veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)) účastníka. Její primární role se aktivuje během roamingových scénářů, zejména když roamingová architektura nepoužívá Local Breakout ([LBO](/mobilnisite/slovnik/lbo/)).

Z architektonického hlediska H-SMF komunikuje s mnoha dalšími síťovými funkcemi (NFs). Během roamingové relace s domovsky směrovaným (Home Routed, [HR](/mobilnisite/slovnik/hr/)) provozem navštívená veřejná pozemní mobilní síť ([VPLMN](/mobilnisite/slovnik/vplmn/)) vybere navštívenou SMF ([V-SMF](/mobilnisite/slovnik/v-smf/)). Tato V-SMF následně naváže referenční bod N16 s H-SMF v HPLMN. H-SMF funguje jako kotvící SMF pro [PDU](/mobilnisite/slovnik/pdu/) relaci (Protocol Data Unit Session). Je zodpovědná za rozhraní s domovskou funkcí řízení zásad ([H-PCF](/mobilnisite/slovnik/h-pcf/)) pro vynucování zásad, s domovskou správou uživatelských dat (H-UDM) pro předplatitelská data a s domovskou účtovací funkcí (H-CHF). H-SMF nakonec připojí relaci k domovské datové síti (např. internetu nebo podnikové síti) prostřednictvím funkce uživatelské roviny (UPF) v HPLMN (H-UPF).

H-SMF pracuje tak, že přijímá požadavky na správu relací od V-SMF přes rozhraní N16. Relaci autorizuje na základě zásad domovského účastníka získaných z H-PCF a H-UDM. Přidělí IP adresu/prefix z pulu domovské sítě a nastaví příslušné zásady QoS. H-SMF poté nařídí H-UPF, aby vytvořila tunel N9 směrem k V-UPF v navštívené síti, čímž vznikne domovsky směrovaná cesta uživatelské roviny: UE <-> (R)AN <-> V-UPF <-> H-UPF <-> Datová síť. Veškerý provoz uživatelské roviny prochází HPLMN, což umožňuje domovskému operátorovi aplikovat konzistentní vynucování zásad, hlubokou kontrolu paketů (DPI) a účtování. H-SMF generuje účtovací záznamy na základě tarifů domovské sítě a hlásí je H-CHF.

Tato architektura zajišťuje, že domovský operátor si zachovává kontrolu nad zásadami relace a aspekty účtování, i když UE roamuje. Kontrastuje s modelem Local Breakout, kde V-SMF v navštívené síti připojuje relaci přímo k místní datové síti a HPLMN poskytuje pouze autorizaci zásad prostřednictvím H-PCF. Model H-SMF je klíčový pro služby vyžadující přístup ke službám specifickým pro domovskou síť (jako je IMS) nebo pro regulatorní požadavky, kdy musí být provoz směrován přes domovskou zemi. Je základním prvkem pro pokročilé roamingové funkce, jako je 5G Edge Computing, kde H-SMF může vybrat aplikační funkci v domovské síti, aby ovlivnila směrování provozu.

## K čemu slouží

H-SMF byla zavedena v Release 16, aby formalizovala a vylepšila architekturu domovského směrování (Home Routed roaming) pro páteřní síť 5G Core (5GC). V dřívějších verzích (Rel-15) byla roamingová architektura 5GC definována, ale role SMF v domovské a navštívené síti nebyly explicitně rozlišeny samostatnými termíny jako H-SMF a V-SMF. To vedlo k potenciální nejednoznačnosti v implementaci a specifikaci. Explicitní definice H-SMF to řeší jasným vymezením odpovědností mezi SMF v domovské a navštívené síti, což je klíčové pro interoperabilní roamingové dohody, konzistentní vynucování zásad a přesné účtování.

Primární problém, který řeší, je zachování kontroly domovské sítě a kontinuity služeb pro roamující účastníky. V 4G EPC plnila podobnou kotvící funkci brána PDN Gateway (PGW) v domovské síti. Architektura založená na službách (SBA) 5GC a oddělení řídicích a uživatelských funkcí si vyžádaly nový, flexibilnější model. H-SMF zajišťuje, že i když UE roamuje, může přistupovat ke službám ukotveným v jeho HPLMN (např. specifickým APN, IMS službám) se stejnými zásadami a účtováním jako v domovské síti. Také umožňuje domovskému operátorovi implementovat bezpečnostní funkce, jako jsou firewally nebo detekce narušení, na domovsky směrovaném provozu.

Dále je koncept H-SMF zásadní pro vývoj služeb 5G, jako je dělení sítě (network slicing) a edge computing. Roamující UE může požadovat síťový řez (slice), který je instancován pouze v jeho HPLMN. H-SMF je zodpovědná za správu této instance řezu pro roamingovou relaci. Pro edge computing, pokud aplikace vyžaduje výpočetní uzel na hrani domovské sítě (home-edge), H-SMF zprostředkovává připojení k příslušné aplikační funkci v HPLMN. H-SMF tedy umožňuje složité, na služby citlivé roamingové scénáře přesahující jednoduchý přístup k internetu, což bylo omezením méně strukturovaných přístupů.

## Klíčové vlastnosti

- Kotví PDU relace (PDU Sessions) pro roamující koncová zařízení (UE) v architektuře Home Routed
- Komunikuje s H-PCF pro vynucování zásad domovské sítě
- Přiděluje IP adresy/prefixy z pulu domovské sítě
- Generuje účtovací záznamy (CDR) na základě tarifů domovské sítě
- Vybere a řídí domovskou UPF (H-UPF) pro kotvení uživatelské roviny
- Umožňuje přístup ke službám specifickým pro domovskou síť (např. IMS) během roamingu

## Související pojmy

- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [V-SMF – Visited Session Management Function](/mobilnisite/slovnik/v-smf/)

## Definující specifikace

- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.542** (Rel-19) — SMF NIDD Service Based Interface Stage 3

---

📖 **Anglický originál a plná specifikace:** [H-SMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-smf/)
