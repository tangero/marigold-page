---
slug: "pdc"
url: "/mobilnisite/slovnik/pdc/"
type: "slovnik"
title: "PDC – Personal Digital Communication"
date: 2025-01-01
abbr: "PDC"
fullName: "Personal Digital Communication"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pdc/"
summary: "Termín používaný ve specifikacích 3GPP, zejména v kontextu testování výkonu kodeků, jako synonymum pro specifický scénář hlasové služby. Často odkazuje na úzkopásmový telefonní servisní model používan"
---

PDC je termín 3GPP pro úzkopásmový telefonní servisní model používaný jako specifický scénář hlasové služby při testování výkonu kodeků pro hodnocení kvality řeči.

## Popis

V terminologii 3GPP je Personal Digital Communication (PDC) odkazováno primárně v rámci specifikací testování výkonu hlasových kodeků, zejména v řadě 26 (Codec specific conformance testing). Používá se jako označení pro specifický testovací scénář nebo servisní podmínky. Technicky PDC v tomto kontextu modeluje digitální buněčnou telefonní službu, historicky podobnou určitým systémům 2G, ale v rámci testů 3GPP definuje sadu síťových podmínek a audio charakteristik, vůči kterým se měří výkon kodeku.

Testovací architektura zahrnuje aplikaci testovaného kodeku (např. [AMR](/mobilnisite/slovnik/amr/), [AMR-WB](/mobilnisite/slovnik/amr-wb/), [EVS](/mobilnisite/slovnik/evs/)) na řečové vzorky, které byly zpracovány tak, aby simulovaly scénář služby PDC. To zahrnuje specifické charakteristiky, jako je akustické rozhraní (např. typický telefon s jeho frekvenční charakteristikou), podmínky okolního hluku a potenciálně specifické vzory bitových chyb nebo modely ztráty paketů reprezentativní pro starší digitální buněčný kanál. Výstup je následně hodnocen pomocí percepčních metrik kvality (např. [POLQA](/mobilnisite/slovnik/polqa/)), aby bylo zajištěno, že kodek splňuje minimální požadavky na výkon za těchto definovaných podmínek 'PDC'.

Jeho role je zajistit interoperabilitu kodeků a kvalitu napříč řadou historických a simulovaných síťových prostředí. Zařazením PDC jako testovacího scénáře 3GPP zaručuje, že moderní kodeky nasazené v sítích 3G, 4G a 5G mohou stále poskytovat přijatelnou kvalitu řeči při propojení s podmínkami připomínajícími starší digitální buněčné technologie nebo při jejich provozu. To je součástí širší sady testovacích scénářů včetně podmínek '3G', '4G' a 'VoIP' definovaných ve specifikacích jako TS 26.131 a TS 26.132.

## K čemu slouží

Termín PDC se používá v rámci frameworku konformního testování 3GPP k udržení komplexní sady referenčních hodnot kvality pro hlasové kodeky. Existuje proto, aby zajistil zpětnou kompatibilitu a robustní výkon napříč vývojovou cestou mobilních sítí. Jak se sítě vyvíjely od 2G k 5G, byly zaváděny nové hlasové kodeky, ale stále musely spolehlivě fungovat za kanálových podmínek, se kterými se lze setkat při přechodech na starší sítě nebo ve scénářích smíšeného nasazení.

Řeší problém neúplného hodnocení kvality. Testování kodeků pouze za ideálních nebo moderních síťových podmínek (např. čisté LTE) by neodhalilo, jak degradují v hlučnějším, náchylnějším k chybám prostředí charakteristickém pro starší digitální systémy. Přesným definováním scénáře PDC poskytuje 3GPP výrobcům zařízení a testovacím laboratořím reprodukovatelnou, standardizovanou sadu podmínek. Tím je zajištěno, že všechna certifikovaná UE a síťové prvky používající daný kodek poskytnou konzistentní minimální kvalitu řeči, a to i při suboptimálních rádiových podmínkách, čímž je chráněn uživatelský zážitek.

## Klíčové vlastnosti

- Definuje specifický testovací scénář pro hodnocení výkonu hlasových kodeků
- Modeluje akustické a síťové podmínky starší digitální buněčné služby
- Používá se spolu s percepčními metodami hodnocení kvality řeči (např. POLQA)
- Součást povinného konformního testování pro hlasové kodeky 3GPP
- Zajišťuje robustnost kodeku za definované sady neideálních podmínek
- Podporuje interoperabilitu napříč generacemi síťové technologie

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [POLQA – Perceptual Objective Listening Quality Assessment](/mobilnisite/slovnik/polqa/)

## Definující specifikace

- **TS 26.101** (Rel-19) — Generic frame format for AMR and GSM-EFR speech codecs
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.470** (Rel-19) — F1 Interface Introduction
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [PDC na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdc/)
