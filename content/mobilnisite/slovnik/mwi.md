---
slug: "mwi"
url: "/mobilnisite/slovnik/mwi/"
type: "slovnik"
title: "MWI – Message Waiting Indication"
date: 2026-01-01
abbr: "MWI"
fullName: "Message Waiting Indication"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mwi/"
summary: "Doplňková služba v sítích IMS a CS, která uživatele (např. prostřednictvím vizuálního ukazatele či oznámení) upozorní, že v síťové schránce čeká jedna nebo více nových zpráv. Je klíčovou funkcí pro sl"
---

MWI (Message Waiting Indication) je doplňková služba v sítích IMS a CS, která uživatele upozorní, že v síťové schránce čekají nové zprávy, a zlepšuje tak služby jako hlasová pošta.

## Popis

Message Waiting Indication (MWI) je standardizovaná doplňková služba definovaná v rámci 3GPP, primárně pro IP Multimedia Subsystem (IMS) a sítě s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)). Jejím hlavním účelem je informovat uživatelské zařízení (UE), že nová zpráva, například hlasová či multimediální zpráva, byla uložena v síťové schránce a čeká na vyzvednutí. Samotná indikace je síťově spuštěné oznámení, nikoli obsah zprávy. Z architektonického hlediska zahrnuje MWI několik síťových entit. Úložiště zpráv (např. server hlasové pošty nebo Multimedia Messaging Service Centre - MMSC) detekuje novou zprávu pro účastníka. Tuto událost pak signalizuje, typicky přes IP Multimedia Subsystem (IMS) nebo jádro CS, službě řízení služeb. V IMS se na tom často podílí aplikační server ([AS](/mobilnisite/slovnik/as/)) hostující službu MWI. AS je zodpovědný za generování a správu předplatného MWI a oznámení. Oznámení je pak doručeno uživatelskému zařízení (UE) pomocí specifických protokolů. Pro MWI založené na IMS se uživatelské zařízení přihlásí k odběru balíčku událostí MWI podle definice v RFC 3842 pomocí metody SIP SUBSCRIBE směřované k AS MWI. AS pak při změně stavu čekajících zpráv (např. příchodu nové zprávy nebo přečtení všech zpráv) zasílá uživatelskému zařízení zprávy SIP NOTIFY. Zpráva NOTIFY obsahuje XML tělo, které podrobně popisuje stav čekajících zpráv, například počet nových a starých zpráv. V sítích CS může být MWI signalizováno prostřednictvím mechanismů jako Feature Indication v signalizaci řízení hovoru nebo specifickými tóny. Uživatelské zařízení po přijetí platného oznámení MWI aktivuje lokální ukazatel (například ikonu na obrazovce), aby upozornilo uživatele. Služba je těsně integrována s dalšími službami IMS, jako je Voice over LTE (VoLTE) a Rich Communication Services (RCS), což zajišťuje konzistentní zážitek ze zasílání zpráv napříč různými přístupovými sítěmi. Bezpečnost a soukromí jsou zachovány, protože oznámení je součástí autentizovaného SIP dialogu mezi uživatelským zařízením a AS.

## K čemu slouží

MWI bylo vytvořeno k vyřešení zásadního problému uživatelského zážitku v telefonních a zprávových systémech: uživatel neměl způsob, jak zjistit, zda obdržel novou hlasovou zprávu nebo zprávu, aniž by manuálně zkontroloval svou schránku. To bylo neefektivní a vedlo k opožděnému vyzvednutí zpráv. V éře základní mobilní telefony byl občas jako primitivní MWI používán přerušovaný vyzváněcí tón na lince, ale tento přístup nebyl standardizovaný ani spolehlivý napříč sítěmi a zařízeními. Formální standardizace MWI v rámci 3GPP, počínaje Release 7 s IMS, poskytla jednotný, interoperabilní mechanismus. Řešila omezení proprietárních řešení dodavatelů a umožnila bezproblémový roaming služeb. Motivací bylo zvýšit hodnotu síťových zprávových služeb (hlasová pošta, [MMS](/mobilnisite/slovnik/mms/)) tím, že se učiní proaktivními, a tím se zvýší jejich využití a užitečnost. Jak se sítě vyvíjely k plně IP architekturám s IMS, stalo se MWI klíčovou součástí pro dosažení funkční parity služeb se staršími [CS](/mobilnisite/slovnik/cs/) sítěmi a pro umožnění pokročilých scénářů multimediálního zasílání zpráv. Zajišťuje, že uživatelé okamžitě dostávají vizuální potvrzení o čekajících zprávách, které je hladce integrováno s nativním rozhraním telefonu, což je zásadní pro moderní komunikační služby.

## Klíčové vlastnosti

- Standardizovaný balíček událostí pro předplatné a oznámení založené na SIP (RFC 3842/3GPP)
- Podpora implementací pro sítě IMS (SIP) i s přepojováním okruhů (CS)
- XML shrnutí zpráv v tělech NOTIFY s detaily o počtu a typech zpráv
- Síťově spuštěná aktualizace stavu při změně stavu schránky
- Integrace se systémy hlasové pošty a centry služby multimediálních zpráv (MMSC)
- Umožňuje vizuální nebo zvukové ukazatele na uživatelském zařízení (UE)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.606** (Rel-19) — MWI Service Protocol Description
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony
- **TS 32.275** (Rel-19) — MMTel Charging Specification
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study

---

📖 **Anglický originál a plná specifikace:** [MWI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mwi/)
