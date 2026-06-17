---
slug: "dpck-id"
url: "/mobilnisite/slovnik/dpck-id/"
type: "slovnik"
title: "DPCK-ID – MCData Payload Cipher Key Identifier"
date: 2025-01-01
abbr: "DPCK-ID"
fullName: "MCData Payload Cipher Key Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dpck-id/"
summary: "DPCK-ID je identifikátor používaný ve službách 3GPP Mission Critical Data (MCData) k jednoznačnému odkazování na konkrétní šifrovací klíč užitečného zatížení MCData (DPCK). Umožňuje komunikujícím konc"
---

DPCK-ID je identifikátor používaný ve službách 3GPP Mission Critical Data k jednoznačnému odkazování na konkrétní šifrovací klíč užitečného zatížení MCData (MCData Payload Cipher Key), který koncovým bodům umožňuje vybrat správný klíč pro dešifrování zašifrovaného datového užitečného zatížení.

## Popis

Identifikátor šifrovacího klíče užitečného zatížení MCData (DPCK-ID) je klíčovou součástí protokolu pro správu klíčů a signalizaci zabezpečení ve službách 3GPP Mission Critical Data. Jedná se o jedinečnou značku nebo odkaz spojený s konkrétní instancí šifrovacího klíče užitečného zatížení MCData ([DPCK](/mobilnisite/slovnik/dpck/)). Samotný DPCK-ID není tajnou hodnotou; je přenášen v otevřené podobě v signalizačních nebo hlavičkových informacích zprávy MCData. Jeho jediným účelem je naznačit přijímající entitě, který z potenciálně více uložených DPCK by měl být použit k dešifrování přiloženého zašifrovaného užitečného zatížení.

V praxi, když aplikační server MCData nebo UE potřebuje odeslat zašifrovanou datovou zprávu, zašifruje užitečné zatížení pomocí aktuálně aktivního DPCK. Poté zahrne odpovídající DPCK-ID do metadat zprávy (např. do specifické bezpečnostní hlavičky definované v TS 24.582). Po přijetí klient MCData příjemce analyzuje DPCK-ID, vyhledá ve svém lokálním úložišti klíčů DPCK s tímto identifikátorem a použije nalezený klíč k provedení dešifrování. Tento mechanismus je zásadní v dynamických scénářích skupinové komunikace, kde mohou být klíče aktualizovány, obnovovány nebo kde se pro různé skupiny nebo relace používají různé klíče.

Správu vazby mezi DPCK a jeho DPCK-ID zajišťuje funkce správy klíčů (KMF) nebo entita odpovědná za distribuci klíčů. Když je vygenerován nový DPCK a distribuován členům skupiny (např. po obnovení klíče nebo když se nový uživatel připojí ke skupině), distribuční protokol sděluje jak materiál klíče, tak jeho přidružený DPCK-ID. Identifikátor musí být synchronizován napříč všemi autorizovanými entitami, které klíč vlastní. Struktura a formát DPCK-ID jsou definovány v příslušných specifikacích 3GPP, aby byla zajištěna interoperabilita.

## K čemu slouží

DPCK-ID byl zaveden spolu s [DPCK](/mobilnisite/slovnik/dpck/) ve vydání 14, aby vyřešil problém identifikace klíče v skupinové, zabezpečené komunikaci MCData. V systému, kde může být současně aktivních více šifrovacích klíčů (např. pro různé mluvčí skupiny, pro různé časové relace nebo jako výsledek periodických aktualizací klíčů), je vyžadován jednoduchý mechanismus signalizace, který klíč byl použit pro šifrování. Bez explicitního identifikátoru by přijímače musely provádět pokusné dešifrování všemi dostupnými klíči, což je neefektivní, zvyšuje latenci a mohlo by vést k provozním selháním.

Jeho vytvoření bylo motivováno potřebou robustní a škálovatelné správy klíčů pro aplikace kritické pro činnost. Použití identifikátoru umožňuje plynulé obnovování klíčů bez přerušení služby: nový klíč s novým ID může být distribuován před vypršením platnosti starého. Zprávy zašifrované starým klíčem mohou být stále dešifrovány, pokud je klíč a jeho ID uchovány po dobu odkladu. DPCK-ID umožňuje základní princip „kryptografického oddělení“, což systému dovoluje spravovat portfolio klíčů pro různé bezpečnostní kontexty a zajišťuje, že je vždy použit správný klíč, což je zásadní pro spolehlivost a zabezpečení požadované orgány veřejné bezpečnosti.

## Klíčové vlastnosti

- Jednoznačně identifikuje konkrétní instanci šifrovacího klíče užitečného zatížení MCData (DPCK)
- Přenášen v otevřené podobě v signalizačních hlavičkách zprávy MCData
- Umožňuje přijímačům vybrat správný klíč z lokálního úložiště pro dešifrování
- Zásadní pro podporu aktualizací klíčů, jejich obnovování a více souběžných klíčů
- Formát a použití definovány ve specifikacích signalizace 3GPP MCData
- Spravován a distribuován ve spojení s DPCK entitami správy klíčů

## Související pojmy

- [DPCK – MCData Payload Cipher Key](/mobilnisite/slovnik/dpck/)

## Definující specifikace

- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols

---

📖 **Anglický originál a plná specifikace:** [DPCK-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpck-id/)
