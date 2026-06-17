---
slug: "msua"
url: "/mobilnisite/slovnik/msua/"
type: "slovnik"
title: "MSUA – MWI Subscriber User Agent"
date: 2025-01-01
abbr: "MSUA"
fullName: "MWI Subscriber User Agent"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/msua/"
summary: "MSUA je funkční entita v rámci IP Multimedia Subsystem (IMS), která jedná jménem účastníka při správě služeb indikace čekajících zpráv (MWI). Přihlašuje se k odběru notifikací událostí MWI ze sítě a s"
---

MSUA je funkční entita v IMS, která jedná za účastníka při správě služeb indikace čekajících zpráv (MWI) tím, že se přihlásí k odběru síťových notifikací a stav (např. upozornění na hlasovou poštu) prezentuje uživateli.

## Popis

[MWI](/mobilnisite/slovnik/mwi/) Subscriber User Agent (MSUA) je funkční entita na straně klienta definovaná ve specifikacích 3GPP pro IP Multimedia Subsystem (IMS), konkrétně v TS 24.173 (IMS Management Object), TS 24.406 (Messaging service) a TS 24.606 (Message Waiting Indication). Funguje jako specializovaný User Agent (UA), který zpracovává služby indikace čekajících zpráv (MWI) pro účastníka IMS. MWI je služba, která uživatele informuje (např. prostřednictvím vizuální ikony na telefonu), že nové zprávy, jako jsou hlasové nebo multimediální zprávy, čekají v síťové poštovní schránce. MSUA je zodpovědná za procedury přihlášení k odběru a notifikace spojené s touto událostí.

Z architektonického hlediska se MSUA nachází v User Equipment (UE) nebo v aplikačním serveru jednajícím jménem uživatele. Její fungování je založeno na rámci pro notifikace událostí v IMS definovaném balíčkem událostí SIP pro MWI (RFC 3842). MSUA zahajuje proces odesláním požadavku SIP SUBSCRIBE příslušnému MWI serveru (často Messaging Server nebo vyhrazený Application Server). Tento požadavek na přihlášení k odběru obsahuje identitu uživatele (např. SIP URI) a specifikuje balíček událostí MWI. Po úspěšném přihlášení bude síť (MWI server) posílat zprávy SIP NOTIFY k MSUA vždy, když se stav čekajících zpráv změní – například při příchodu nové hlasové zprávy nebo po vyzvednutí všech zpráv.

MSUA tyto zprávy NOTIFY zpracovává; ty obsahují tělo XML s detaily o stavu čekajících zpráv (např. počet nových vs. starých zpráv, typ zprávy). Agent následně tyto informace prezentuje koncovému uživateli prostřednictvím uživatelského rozhraní zařízení. MSUA také spravuje životní cyklus odběru, včetně obnovení odběru před jeho vypršením a opětovného přihlášení po síťových nebo zařízení selháních. Její role je klíčová pro poskytování plynulé, reálné indikace stavu zpráv, která integruje služby hlasové pošty a dalších zpráv do jednotného servisního prostředí IMS. Abstrahuje složitost signalizace SIP od hlavního uživatelského agenta používaného pro hlasové nebo videohovory, což umožňuje specializované zpracování událostí spojených se zprávami.

## K čemu slouží

MSUA byla vytvořena za účelem standardizace a umožnění služeb indikace čekajících zpráv ([MWI](/mobilnisite/slovnik/mwi/)) v rámci architektury IP Multimedia Subsystem (IMS). Před IMS a standardizovaným zpracováním MWI byly notifikace hlasové pošty často doručovány různými, někdy proprietárními metodami – například speciálními SMS zprávami nebo signálními tóny v okruhově spínaných sítích. To vedlo k roztříštěnému uživatelskému zážitku a ztěžovalo implementaci jednotné komunikace napříč různými sítěmi a typy zařízení. Jelikož IMS usilovala o konvergenci různých komunikačních služeb (hlas, video, zprávy) přes IP, byl nezbytný konzistentní mechanismus založený na SIP pro upozorňování uživatelů na čekající zprávy.

MSUA řeší problém, jak může být zařízení účastníka IMS proaktivně a spolehlivě informováno o stavu síťové poštovní schránky. Využívá stávající model přihlášení/notifikace IMS, který je efektivní a škálovatelný, a vyhýbá se tak potřebě neustálého dotazování ze strany zařízení. Tím se snižuje síťový provoz a spotřeba baterie na UE. Vytvoření vyhrazené funkční entity (MSUA) umožňuje jasné oddělení odpovědností: hlavní IMS UA zpracovává služby založené na relacích, jako jsou hovory, zatímco MSUA se specializuje na asynchronní zpracování událostí pro zprávy. Tato modularita zjednodušuje návrh klientského softwaru a zajišťuje robustní zpracování událostí MWI, i když je právě aktivní hlasový hovor.

Zavedená ve verzi 7 (Release 7) byla specifikace MSUA součástí širšího úsilí o dozrání služeb zasílání zpráv a presence založených na IMS. Odstranila omezení dřívějších nestandardizovaných notifikací tím, že poskytla interoperabilní, sítí řízenou metodu. To umožnilo operátorům nabízet rozšířené služby hlasové pošty s vizuálními indikátory na široké škále zařízení, což zlepšilo uživatelský komfort. Navíc díky použití SIP umožnila integraci MWI s dalšími službami IMS, jako je kombinace stavu hlasové pošty s informacemi o přítomnosti. MSUA je tedy klíčovým prvkem pro bohatý, jednotný komunikační zážitek slibovaný IMS, který zajišťuje, že uživatelé jsou neprodleně informováni o důležitých zprávách bez ohledu na jejich aktuální činnost na zařízení.

## Klíčové vlastnosti

- Funkční entita, která se přihlašuje k odběru notifikací událostí MWI pomocí SIP SUBSCRIBE
- Zpracovává zprávy SIP NOTIFY obsahující stav čekajících zpráv ve formátu XML
- Prezentuje stav MWI (např. ikona hlasové pošty, počet zpráv) koncovému uživateli
- Spravuje životní cyklus odběru včetně obnovení a zotavení z chyb
- Funguje na základě rámce pro notifikace událostí v IMS (RFC 3842)
- Může sídlit v User Equipment nebo v síťovém aplikačním serveru jednajícím jménem uživatele

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.606** (Rel-19) — MWI Service Protocol Description

---

📖 **Anglický originál a plná specifikace:** [MSUA na 3GPP Explorer](https://3gpp-explorer.com/glossary/msua/)
