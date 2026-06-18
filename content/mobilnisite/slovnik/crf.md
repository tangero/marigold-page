---
slug: "crf"
url: "/mobilnisite/slovnik/crf/"
type: "slovnik"
title: "CRF – Charging Rules Function"
date: 2025-01-01
abbr: "CRF"
fullName: "Charging Rules Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/crf/"
summary: "Funkce pravidel účtování (CRF) je základní síťový prvek zodpovědný za autorizaci a poskytování pravidel účtování funkci prosazování politik a účtování (PCEF). Určuje, jak mají být uživatelské relace ú"
---

CRF je základní síťový prvek, který autorizuje a poskytuje pravidla účtování funkci PCEF, a určuje, jak mají být uživatelské relace účtovány na základě profilů účastníka, využití služeb a síťových politik.

## Popis

Funkce pravidel účtování (CRF) je klíčovou součástí architektury řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) dle 3GPP, konkrétně definovanou ve frameworku Release 6 a zachovávanou v následujících vydáních. Funguje jako centrální logická entita, která rozhoduje o tom, jak má být účtování aplikováno na jednotlivé relace [IP-CAN](/mobilnisite/slovnik/ip-can/) (IP Connectivity Access Network). CRF přijímá informace o službě od aplikační funkce ([AF](/mobilnisite/slovnik/af/)) a informace o účastníkovi z úložiště profilů předplatného ([SPR](/mobilnisite/slovnik/spr/)), následně tyto údaje kombinuje s operátorem definovanými politikami za účelem generování konkrétních pravidel účtování.

Z architektonického hlediska CRF rozhraní s několika klíčovými prvky PCC prostřednictvím standardizovaných referenčních bodů. Rozhraní Rx spojuje CRF s aplikační funkcí (AF), což umožňuje AF komunikovat informace specifické pro službu, které mohou ovlivnit rozhodnutí o účtování. Rozhraní Sp poskytuje přístup k účastnickým datům uloženým v SPR, včetně profilů služeb, povolených služeb a parametrů souvisejících s účtováním. Nejvýznamnější je, že CRF komunikuje s funkcí prosazování politik a účtování ([PCEF](/mobilnisite/slovnik/pcef/)) prostřednictvím rozhraní Gx, přes které zřizuje autorizovaná pravidla účtování k prosazení.

Činnost CRF sleduje dobře definovanou sekvenci. Když uživatel naváže relaci IP-CAN, PCEF typicky požaduje pravidla účtování od CRF. CRF vyhodnocuje více vstupů: profil účastníka z SPR, veškeré informace o službě od AF a pravidla politik síťového operátora. Na základě tohoto vyhodnocení určuje příslušné parametry účtování, jako je metoda účtování (online, offline nebo obojí), ratingové skupiny, identifikátory služeb a použitelné prahové hodnoty. Tyto parametry jsou zapouzdřeny v [AVP](/mobilnisite/slovnik/avp/) (atribut-hodnota) definice pravidel účtování a odeslány do PCEF k implementaci.

V rámci pravidel účtování CRF specifikuje, zda se použije online účtování (interaktivní, na bázi kreditu) prostřednictvím online systému účtování ([OCS](/mobilnisite/slovnik/ocs/)), nebo offline účtování (dávkové zpracování) prostřednictvím offline systému účtování ([OFCS](/mobilnisite/slovnik/ofcs/)). Pro online účtování definuje parametry řízení kreditu a pravidla správy kvót. Pro offline účtování specifikuje spouštěče generování záznamů účtovacích dat (CDR) a pravidla formátování. CRF může také upravovat pravidla účtování během aktivní relace v reakci na měnící se podmínky, jako je upgrade služby, změna polohy nebo vyčerpání kvóty, čímž zajišťuje, že účtování zůstává v souladu s aktuálním kontextem služby.

Role CRF přesahuje pouhé zřizování pravidel a zahrnuje interakci s politikami. Zatímco funkce pravidel politik a účtování (PCRF) řeší rozhodnutí o politice QoS v pozdějších architekturách, v dřívějších implementacích PCC a specifických nasazeních může CRF zahrnovat rozhodovací logiku politik nebo úzce spolupracovat s funkcemi politik. Tato integrace zajišťuje korelaci pravidel účtování s autorizovanou QoS a zabraňuje situacím, kdy by se politiky účtování a kvality služby dostaly do konfliktu. CRF tedy slouží jako inteligentní rozhodovací bod pro účtování, který převádí obchodní pravidla, nároky účastníků a charakteristiky služeb na technicky vynutitelná instrukce účtování.

## K čemu slouží

CRF byla zavedena ve 3GPP Release 6 jako součást komplexní architektury řízení politik a účtování (PCC) za účelem řešení omezení dřívějších účtovacích systémů při zpracování různorodých služeb na bázi IP. Před PCC byly účtovací mechanismy často statické, specifické pro službu a těsně provázané se síťovými prvky, což ztěžovalo implementaci flexibilního, reálného účtování pro nově vznikající multimediální služby. Operátoři potřebovali centralizovaný, dynamický systém, který by dokázal přizpůsobit účtování na základě skutečného využití služeb, profilů účastníků a síťových podmínek.

Primární problém, který CRF řeší, je oddělení účtovací logiky od vymáhacích funkcí, což umožňuje sofistikovanější modely účtování. Bez CRF by musela být pravidla účtování předem nakonfigurována v síťových prvcích, což by omezovalo schopnost operátorů nabízet personalizované účtovací plány, upgrady služeb v reálném čase nebo kontextově citlivé fakturace. CRF poskytuje inteligenci pro dynamické rozhodování o účtování s ohledem na faktory jako typ služby, hodnota obsahu, denní doba, úroveň účastníka a zbývající zůstatky.

Historicky bylo vytvoření CRF motivováno přechodem od služeb hlasové komunikace s přepojováním okruhů k paketovým multimediálním službám v sítích 3G. Tento posun vyžadoval účtovací systémy schopné zpracovat proměnné přenosové rychlosti, více současných služeb a diferenciaci na základě kvality. CRF jako součást frameworku PCC umožnila operátorům zpeněžit nové služby, jako je streamování videa, hraní her a podnikové aplikace, prostřednictvím podrobného, politikami řízeného účtování namísto jednoduchého účtování na základě objemu. Poskytla základnu pro sítě s povědomím o službách, kde mohlo být účtování sladěno jak se spotřebou síťových zdrojů, tak s vnímanou hodnotou služeb pro účastníky.

## Klíčové vlastnosti

- Dynamická autorizace pravidel účtování na základě více vstupů
- Integrace s aplikační funkcí (AF) pro účtování s povědomím o službě
- Přístup k profilům účastníků prostřednictvím úložiště profilů předplatného (SPR)
- Zřizování pravidel účtování pro PCEF prostřednictvím rozhraní Gx
- Podpora online i offline metod účtování
- Relací založené účtování se schopností modifikace během relace

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)

## Definující specifikace

- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification

---

📖 **Anglický originál a plná specifikace:** [CRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/crf/)
