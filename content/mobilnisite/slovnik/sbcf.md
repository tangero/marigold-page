---
slug: "sbcf"
url: "/mobilnisite/slovnik/sbcf/"
type: "slovnik"
title: "SBCF – Session Based Charging Function"
date: 2025-01-01
abbr: "SBCF"
fullName: "Session Based Charging Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sbcf/"
summary: "SBCF je klíčová komponenta v online účtovacím systému (OCS) dle 3GPP. Je zodpovědná za správu řízení kreditu pro servisní relace v reálném čase, komunikuje s síťovými elementy za účelem autorizace, mo"
---

SBCF je funkce pro účtování na základě relace (Session Based Charging Function), klíčová komponenta online účtovacího systému (OCS) dle 3GPP, která spravuje řízení kreditu v reálném čase pro servisní relace tím, že je autorizuje, monitoruje a ukončuje na základě kreditu účastníka a příslušných politik.

## Popis

Funkce pro účtování na základě relace (SBCF) je základní logická funkce v architektuře online účtovacího systému ([OCS](/mobilnisite/slovnik/ocs/)) dle 3GPP, jak je definováno v sérii standardů pro telekomunikační management (TS 32.2xx). Funguje jako centrální mechanismus pro řízení kreditu v reálném čase na bázi relací. SBCF komunikuje se síťovými elementy známými jako funkce spouštějící účtování ([CTF](/mobilnisite/slovnik/ctf/)) – například [P-GW](/mobilnisite/slovnik/p-gw/), [S-CSCF](/mobilnisite/slovnik/s-cscf/) nebo [MME](/mobilnisite/slovnik/mme/) – prostřednictvím standardizovaného referenčního bodu Ro za použití protokolu Diameter Credit Control Application ([DCCA](/mobilnisite/slovnik/dcca/)). Když účastník zahájí servisní relaci (např. hovor, datovou relaci, IMS relaci), CTF odešle SBCF požadavek na řízení kreditu. SBCF následně provede tarifikaci na základě profilu účastníka, detailů služby a tarifních plánů a rezervuje odpovídající částku kreditu z účtu účastníka.

Po úspěšné rezervaci kreditu SBCF přidělí síťovému elementu kvótu (např. objem dat, časové trvání), čímž autorizuje poskytnutí služby. Síťový element následně monitoruje spotřebu zdrojů vůči této kvótě. Jak je kvóta spotřebovávána, CTF může odesílat průběžné aktualizační požadavky SBCF, aby nahlásila spotřebu a požádala o další kredit. SBCF tyto aktualizace spravuje, případně provádí přecenění, a přiděluje nové kvóty. Tento proces pokračuje až do ukončení relace nebo vyčerpání kreditu účastníka. Pokud dojde kredit, SBCF nařídí síťovému elementu ukončit nebo přesměrovat servisní relaci. Během celého tohoto cyklu SBCF generuje účtovací události, které jsou předávány funkci brány pro účtování ([CGF](/mobilnisite/slovnik/cgf/)) nebo přímo do fakturační domény pro konečný výpočet účtu.

Z architektonického hlediska je SBCF často implementována jako součást většího uzlu OCS společně s dalšími funkcemi, jako je funkce správy zůstatku na účtu ([ABMF](/mobilnisite/slovnik/abmf/)) a funkce tarifikace (RF). Hraje klíčovou roli při umožňování předplacených služeb, kontrol výdajových limitů a vynucování politik v reálném čase. Dynamickou správou relací umožňuje operátorům nabízet složité tarifní plány, jako jsou stupňované datové balíčky, časově závislé sazby a služebně specifické účtování, a zároveň zaručuje, že nedojde ke ztrátě příjmů z nezaplaceného využití. Její fungování je zásadní pro konvergenci účtování napříč přístupovými technologiemi (2G/3G/4G/5G) a servisními doménami (hlas, data, zprávy, IMS).

## K čemu slouží

SBCF byla vytvořena, aby odstranila omezení tradičního offline (postpaidního) účtování, které nedokázalo zabránit využívání služeb v případě, že účastník neměl dostatek financí nebo kreditu. To představovalo pro operátory významné obchodní riziko, zejména s nástupem předplacených mobilních služeb. Rané předplacené systémy byly často proprietární, izolované a nedokázaly snadno podporovat nové služby nebo konvergentní účtování napříč více typy služeb. Standardizace OCS a SBCF ve 3GPP Release 5 (pro IMS) a její ustálení v Release 8 poskytly jednotný rámec pro účtování v reálném čase.

Primární motivací bylo umožnit operátorům nabízet inovativní předplacené a hybridní platební modely pro všechny služby, včetně nově se objevujících služeb založených na IP, jako je IMS a mobilní data, škálovatelným a interoperabilním způsobem. SBCF to řeší tím, že poskytuje standardizovaný mechanismus řízení kreditu s ohledem na relaci. Umožňuje okamžitou autorizaci a průběžnou kontrolu spotřeby zdrojů, čímž chrání příjmy operátora. Dále podporuje konvergenci účtování pro hlasové, datové a multimediální služby na jedinou platformu, což zjednodušuje provoz a umožňuje personalizované tarifní plány v reálném čase, které zlepšují zákaznický zážitek a loajalitu.

## Klíčové vlastnosti

- Řízení a rezervace kreditu v reálném čase pro servisní relace
- Komunikuje se síťovými CTF prostřednictvím rozhraní Diameter Ro
- Přiděluje a spravuje kvóty využití (objem, čas, události)
- Provádí tarifikaci a přecenění na bázi relací
- Vynucuje výdajové limity a politiky řízení
- Generuje účtovací události pro fakturační systém

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [CTF – Charging Trigger Function](/mobilnisite/slovnik/ctf/)
- [ABMF – Accounting Balance Management Function](/mobilnisite/slovnik/abmf/)

## Definující specifikace

- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.296** (Rel-19) — Online Charging System (OCS) Architecture
- **TS 32.825** (Rel-10) — Study on Rc Reference Point for ABMF

---

📖 **Anglický originál a plná specifikace:** [SBCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbcf/)
