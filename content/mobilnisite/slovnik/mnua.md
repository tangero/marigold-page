---
slug: "mnua"
url: "/mobilnisite/slovnik/mnua/"
type: "slovnik"
title: "MNUA – MWI Notifier User Agent"
date: 2025-01-01
abbr: "MNUA"
fullName: "MWI Notifier User Agent"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mnua/"
summary: "Funkční entita v rámci IP Multimedia Subsystem (IMS), která funguje jako klient pro službu oznámení o čekající zprávě (MWI). Nachází se v uživatelském zařízení (UE) a je zodpovědná za přihlášení k odb"
---

MNUA je funkční entita v uživatelském zařízení IMS, která funguje jako klient pro přihlášení k odběru a zpracování oznámení o čekající zprávě (Message Waiting Indication), například o nových hlasových zprávách.

## Popis

[MWI](/mobilnisite/slovnik/mwi/) Notifier User Agent (MNUA) je SIP aplikační klient definovaný v servisním rámci IMS (konkrétně v TS 24.173 pro MWI a souvisejících specifikacích). Jedná se o typ User Agent (UA), který implementuje roli odběratele pro službu oznámení o čekající zprávě. MNUA sídlí v uživatelském zařízení (UE) s podporou IMS, jako je smartphone nebo VoIP stolní telefon. Jeho hlavní funkcí je interakce s odpovídající síťovou funkční entitou, MWI Notifier Server, za účelem přijímání oznámení o stavu uživatelovy úschovny zpráv (typicky serveru hlasových zpráv).

MNUA funguje pomocí rámce pro oznamování událostí v SIP (RFC 6665, známé jako SUBSCRIBE/NOTIFY). Proces začíná tím, že MNUA odešle požadavek SIP SUBSCRIBE směrem k MWI Notifier Server. Tento odběr je směrován na konkrétní SIP URI, která reprezentuje uživatelovu úschovnu zpráv (např. sip:user@domain.com;mwi). Požadavek na odběr obsahuje hlavičkové pole Event nastavené na 'message-summary', což indikuje zájem o události MWI. Po úspěšném přihlášení k odběru bude síťový server odesílat MNUA požadavky SIP NOTIFY vždy, když se změní stav čekající zprávy (např. příchozí nová hlasová zpráva, poslech nebo smazání hlasové zprávy).

Tělo zprávy NOTIFY obsahuje skutečné informace MWI formátované v XML formátu definovaném balíčkem událostí 'message-summary'. Tato data zahrnují podrobnosti jako počet nových zpráv, počet starých (uložených) zpráv a volitelně i důležitost zpráv. MNUA je zodpovědná za analýzu tohoto XML obsahu, extrakci relevantních stavových informací a jejich prezentaci koncovému uživateli prostřednictvím uživatelského rozhraní zařízení (např. zobrazení ikony hlasové pošty, ukázání počtu zpráv). MNUA také spravuje životní cyklus odběru, včetně obnovování odběru před jeho vypršením a opětovného přihlášení po změnách v síti nebo zařízení, aby zajistila nepřetržitou službu oznamování.

## K čemu slouží

MNUA byla vytvořena za účelem poskytnutí standardizovaného, IP-based mechanismu pro oznamování hlasových zpráv v rámci architektury IMS. Před IMS byla oznámení o hlasových zprávách v sítích s přepojováním okruhů často doručována prostřednictvím signalizace nesouvisející s hovorem (např. v GSM pomocí příznaku v Unstructured Supplementary Service Data nebo přes SMS) nebo proprietárními metodami, což mohlo být neefektivní a postrádat bohaté informace. Přechod na plně IP sítě jako LTE a 5G, kde tradiční [CS](/mobilnisite/slovnik/cs/) fallback chybí, si vyžádal novou, spolehlivou službu pro tuto základní funkci.

MNUA jako součást SIP-based služby [MWI](/mobilnisite/slovnik/mwi/) to řeší využitím flexibilního a rozšiřitelného rámce pro události v SIP. Umožňuje okamžitá, sítí spouštěná oznámení, která jsou nezávislá na hlasovém hovoru. To umožňuje bohatší uživatelský zážitek, protože oznámení může nést podrobné souhrny zpráv. Její vytvoření bylo motivováno potřebou replikovat a vylepšit klasické telefonní služby v paketové doméně IMS, což zajišťuje kontinuitu služeb pro uživatele VoLTE a VoNR. Odděluje službu oznamování od podkladové přístupové technologie, což z ní činí řešení odolné vůči budoucím změnám pro konvergované služby zasílání zpráv.

## Klíčové vlastnosti

- SIP User Agent klient implementující balíček událostí 'message-summary'
- Iniciuje požadavky SIP SUBSCRIBE směrem k MWI Notifier Server pro aktualizace stavu
- Zpracovává příchozí požadavky SIP NOTIFY obsahující souhrny zpráv ve formátu XML
- Analyzuje informace MWI (počty nových/starých zpráv, důležitost) pro prezentaci uživateli
- Spravuje obnovování odběru a stav síťové registrace pro kontinuitu služby
- Umožňuje vizuální a/nebo zvukové indikace stavu hlasové pošty na IMS UE

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.606** (Rel-19) — MWI Service Protocol Description

---

📖 **Anglický originál a plná specifikace:** [MNUA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mnua/)
