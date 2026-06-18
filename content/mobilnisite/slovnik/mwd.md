---
slug: "mwd"
url: "/mobilnisite/slovnik/mwd/"
type: "slovnik"
title: "MWD – Message Waiting Data"
date: 2025-01-01
abbr: "MWD"
fullName: "Message Waiting Data"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mwd/"
summary: "MWD je doplňková služba v sítích s přepojováním okruhů a v sítích IMS, která signalizuje účastníkovi čekající hlasovou zprávu. Spouští notifikaci na uživatelském zařízení (např. ikonu hlasové pošty) a"
---

MWD je doplňková služba, která signalizuje účastníkovi čekající hlasovou zprávu a spouští notifikaci na jeho zařízení v přepojování okruhů a v sítích IMS.

## Popis

Message Waiting Data (MWD) je standardizovaný mechanismus v sítích 3GPP, který spravuje indikaci čekajících zpráv (především hlasových) pro účastníka. Jedná se o síťovou službu, která uchovává jednoduchý datový příznak – indikátor čekající zprávy – asociovaný s účastníkovým číslem. Tento příznak se nastaví na 'aktivní', když je do účastníkova mailboxu uložena nová hlasová zpráva, a zruší se, když si účastník zprávu přehraje nebo smaže. Služba funguje napříč více síťovými doménami: původně byla definována pro sítě s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), jako je GSM, a byla rozšířena pro práci v IP Multimedia Subsystem (IMS) pro VoLTE a VoNR.

Z architektonického hlediska je klíčovou funkční entitou Message Waiting Indication Centre (MWIC) nebo, častěji, systém hlasové pošty (který funguje jako MWIC). Když je nahrána hlasová zpráva, server hlasové pošty signalizuje Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) v CS sítích, nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v IMS sítích, aby aktualizoval profil MWD účastníka. Tato aktualizace nastaví indikátor čekající zprávy. Když se zařízení účastníka registruje v síti (např. při zapnutí nebo změně polohy), síť ([MSC](/mobilnisite/slovnik/msc/)/[VLR](/mobilnisite/slovnik/vlr/) v CS, nebo [S-CSCF](/mobilnisite/slovnik/s-cscf/) v IMS) načte profil účastníka z HLR/HSS. Pokud je příznak MWD aktivní, síť zašle zařízení specifickou notifikaci. V CS sítích se to často provádí pomocí zprávy unstructured supplementary service data ([USSD](/mobilnisite/slovnik/ussd/)) nebo signálu v rámci procedur mobility. V IMS se používá [SIP](/mobilnisite/slovnik/sip/) messaging, konkrétně metoda SIP NOTIFY jako součást balíčku událostí Message Waiting Indication.

Úlohou MWD v síti je poskytovat spolehlivou, síťově řízenou notifikační službu, která je nezávislá na proprietárních protokolech platformy hlasové pošty. Zajišťuje interoperabilitu mezi různými síťovými prvky a uživatelskými zařízeními od různých výrobců. Notifikace se na uživatelském telefonu typicky projeví jako ikona hlasové pošty, textové upozornění nebo přerušovaný vytáčecí tón. MWD je klíčovým prvkem uživatelského komfortu pro telefonní služby, protože poskytuje jasnou vizuální nebo auditivní nápovědu, která uživatele vyzve ke kontrole zpráv, čímž zvyšuje využitelnost a spolehlivost systémů hlasové pošty.

## K čemu slouží

MWD bylo vytvořeno za účelem řešení problému standardizovaného, spolehlivého a síťově efektivního notifikování mobilních účastníků o čekajících hlasových zprávách. V raných mobilních sítích, bez standardizované metody, byly notifikace hlasové pošty nespolehlivé nebo závislé na proprietárních řešeních, která bránila interoperabilitě mezi různými síťovými operátory a výrobci telefonů. Účastníci mohli zmeškat důležité zprávy, pokud nezavolali do své schránky hlasové pošty ručně, což snižovalo užitečnost služby.

Historický kontext spočívá v rámci doplňkových služeb GSM, kde bylo MWD definováno jako základní prvek pro vylepšení základní telefonní služby. Jeho vytvoření bylo motivováno potřebou univerzálního 'indikátoru čekající zprávy', který by fungoval bezproblémově, i když účastníci roamovali v různých sítích a používali různé telefony. Centralizací indikačního příznaku v HLR/HSS mohla síť zajistit konzistentní a přenosný stav notifikace. Jak se sítě vyvíjely směrem k plně IP architekturám s IMS, byla služba MWD adaptována (specifikována v TS 29.338 pro rozhraní Sh mezi systémem hlasové pošty a HSS), aby byla zachována tato nezbytná funkcionalita pro VoLTE a VoNR, což zajišťuje kontinuitu služeb od hlasových služeb 2G/3G CS po hlasové služby 4G/5G s přepojováním paketů. Řeší omezení spočívající v absenci nativního, standardního způsobu, jak může aplikační server (hlasová pošta) aktualizovat profil účastníka a spouštět notifikaci zařízení škálovatelným a bezpečným způsobem.

## Klíčové vlastnosti

- Binární indikační příznak stavu čekající zprávy uložený v síti
- Spouštěno systémem hlasové pošty přes standardizovaná rozhraní (např. MAP k HLR, Sh k HSS)
- Doručuje notifikace na uživatelské zařízení prostřednictvím síťové signalizace (USSD, SIP NOTIFY)
- Podporuje jak domény s přepojováním okruhů (GSM/UMTS), tak IMS (VoLTE/VoNR)
- Umožňuje vizuální nebo auditivní indikaci (např. ikona, přerušovaný vytáčecí tón) na telefonu
- Poskytuje kompatibilitu roamingu pro notifikace hlasové pošty napříč sítěmi operátorů

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.272** (Rel-19) — CS Fallback in EPS
- **TS 29.338** (Rel-19) — Diameter protocols for SMS in MME/5GS

---

📖 **Anglický originál a plná specifikace:** [MWD na 3GPP Explorer](https://3gpp-explorer.com/glossary/mwd/)
