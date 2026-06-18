---
slug: "usi"
url: "/mobilnisite/slovnik/usi/"
type: "slovnik"
title: "USI – User Service Information"
date: 2025-01-01
abbr: "USI"
fullName: "User Service Information"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/usi/"
summary: "User Service Information (USI) je datová struktura používaná v sítích 3GPP pro přenos parametrů souvisejících se službou a informací specifických pro uživatele mezi síťovými prvky. Je primárně definov"
---

USI je datová struktura používaná v sítích 3GPP pro přenos parametrů souvisejících se službou a informací specifických pro uživatele mezi síťovými prvky za účelem uplatňování politik, účtování a QoS.

## Popis

User Service Information (USI) je standardizovaný informační prvek ve specifikacích 3GPP, který přenáší podrobnosti o služebním profilu uživatele a kontextu relace. Je přenášen přes různé referenční body, zejména mezi funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) podle definice v 3GPP TS 29.212, a v rámci rozhraní souvisejících s IMS. USI obsahuje atributy popisující vyvolávanou službu, jako je identifikátor služby, mediální komponenty, identifikátory aplikací a data specifická pro účastníka. Tyto informace jsou klíčové pro síť, aby mohla činit informovaná rozhodnutí týkající se vynucování politik, účtování a přidělování prostředků.

Z architektonického hlediska je USI vloženo do protokolových zpráv, jako jsou zprávy Gx Diameter mezi PCRF a PGW/[PCEF](/mobilnisite/slovnik/pcef/). Když uživatel zahájí datovou relaci nebo službu IMS, může příslušná síťová funkce (např. Application Function ([AF](/mobilnisite/slovnik/af/)) v IMS) poskytnout informace o službě PCRF. PCRF poté tyto informace, případně formátované jako USI, použije k odvození a instalaci odpovídajících pravidel Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) na bráně. Tato pravidla určují, jak je zacházeno s provozem v uživatelské rovině, včetně omezení šířky pásma, prioritního značení a metod účtování.

Obsah USI může být velmi podrobný a zahrnovat parametry jako Flow-Description pro identifikaci konkrétních IP toků, parametry QoS jako QoS Class Identifier ([QCI](/mobilnisite/slovnik/qci/)) a Allocation and Retention Priority ([ARP](/mobilnisite/slovnik/arp/)) a informace související s účtováním, například Rating Group a Service Identifier. V IMS může USI také přenášet podrobnosti o relaci ze signalizace [SIP](/mobilnisite/slovnik/sip/), což umožňuje PCRF korelovat řízení politik s konkrétní relací IMS. To umožňuje dynamické řízení politik, kdy jsou síťové prostředky přidělovány a spravovány v reálném čase na základě aktivní služby, což zvyšuje efektivitu sítě a uživatelský zážitek.

USI hraje zásadní roli při umožnění sítí s povědomím o službě. Poskytnutím strukturovaného způsobu komunikace kontextu služby z aplikační vrstvy do transportní vrstvy jádra sítě umožňuje diferencované zacházení s provozem. Například službě streamování videa může být přidělena vyšší priorita a specifický model účtování ve srovnání s best-effort prohlížením webu. Tato schopnost je zásadní pro implementaci pokročilých obchodních modelů, jako je zero-rating, sponzorovaná data a záruky kvality služeb pro prémiové služby.

## K čemu slouží

Vytvoření User Service Information (USI) bylo motivováno potřebou posunu od jednoduchých, statických profilů účastníků k dynamickému, na službu zaměřenému řízení politik a účtování v sítích 3GPP. Rané mobilní datové sítě primárně používaly statické profily QoS založené na APN účastníka. To bylo nedostatečné pro vzestup různorodých služeb založených na IP, jako jsou IMS, VoIP a streamování videa, které vyžadovaly správu prostředků a účtování specifické pro aplikaci v reálném čase.

USI bylo zavedeno jako součást širší architektury Policy and Charging Control (PCC) ve verzi 3GPP Release 7 a dále upřesňováno v následujících verzích. Řeší omezení spočívající v neexistenci standardizovaného, rozšiřitelného kontejneru pro přenos podrobného kontextu služby z aplikační funkce (např. P-CSCF v IMS) k bodu rozhodování o politikách (PCRF) a nakonec k bodu vynucení (PCEF). Před touto standardizací vyžadovala implementace politik specifických pro službu často proprietární rozšíření nebo nebyla možná, což bránilo nasazení nových, inovativních služeb se specifickými síťovými požadavky.

Poskytnutím definované struktury pro tyto informace umožňuje USI operátorům nasazovat sofistikovanou diferenciaci služeb, personalizované tarifní plány a optimalizaci síťových prostředků. Je klíčovým prvkem pro monetizaci služeb přesahujících jednoduché datové balíčky, což umožňuje partnerství s poskytovateli obsahu a vytváření služeb s různými úrovněmi. Jeho vývoj byl spojen s rozšířením rámce PCC na podporu nových služebních paradigmat, včetně síťového slicing a edge computingu v 5G.

## Klíčové vlastnosti

- Standardizovaný kontejner pro parametry specifické pro službu
- Umožňuje dynamické řízení politik na základě aktivní aplikace
- Podporuje podrobné poskytování parametrů QoS (QCI, ARP)
- Přenáší identifikátory související s účtováním (Rating Group, Service ID)
- Usnadňuje korelaci mezi signalizací IMS a politikami v uživatelské rovině
- Rozšiřitelné pro přizpůsobení novým službám a parametrům

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking

---

📖 **Anglický originál a plná specifikace:** [USI na 3GPP Explorer](https://3gpp-explorer.com/glossary/usi/)
