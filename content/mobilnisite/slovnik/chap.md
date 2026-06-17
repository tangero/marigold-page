---
slug: "chap"
url: "/mobilnisite/slovnik/chap/"
type: "slovnik"
title: "CHAP – Challenge Handshake Authentication Protocol"
date: 2026-01-01
abbr: "CHAP"
fullName: "Challenge Handshake Authentication Protocol"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/chap/"
summary: "CHAP je třífázový autentizační protokol používaný k ověření identity síťových přístupových bodů a uživatelského zařízení při navazování spojení. Poskytuje bezpečnou autentizaci bez přenosu hesel v čit"
---

CHAP je třífázový autentizační protokol používaný v systémech 3GPP k bezpečnému ověření identity síťových bodů a uživatelského zařízení během navazování spojení; využívá mechanismus challenge-response bez odesílání hesla v čitelné podobě.

## Popis

Challenge Handshake Authentication Protocol (CHAP) je autentizační mechanismus protokolu Point-to-Point Protocol (PPP), který poskytuje bezpečné ověření identity prostřednictvím třífázového handshake procesu. Na rozdíl od základní autentizace heslem CHAP nikdy nepřenáší skutečné heslo přes síť, místo toho využívá kryptografické hashování k prokázání znalosti sdíleného tajemství. Protokol funguje na principu challenge-response, kdy autentizátor odešle náhodnou výzvu (challenge) protistraně, která následně vypočte odpověď pomocí jednosměrné hashovací funkce (obvykle MD5) aplikované na výzvu kombinovanou se sdíleným tajemstvím. Tato odpověď je odeslána zpět autentizátoru, který provede stejný výpočet a porovná výsledky, čímž ověří identitu protistrany.

Architektura CHAP zahrnuje tři hlavní komponenty: autentizátor (síťová strana), protistrana (klient) a sdílené tajemství známé oběma stranám. Protokol začíná tím, že autentizátor vygeneruje náhodnou výzvu a odešle ji protistraně. Protistrana vypočte odpověď aplikací hashovací funkce na zřetězení výzvy, sdíleného tajemství a identifikátoru. Tato odpověď je přenesena zpět autentizátoru, který nezávisle vypočte očekávanou hodnotu pomocí své uložené kopie sdíleného tajemství. Pokud se hodnoty shodují, autentizace uspěje; jinak je spojení ukončeno.

V systémech 3GPP je CHAP implementován v rámci různých síťových prvků a rozhraní pro zabezpečení různých typů spojení. Je zvláště důležitý pro aktivaci PDP (Packet Data Protocol) kontextu, kde autentizuje mobilní zařízení pokoušející se navázat datové relace. Protokol podporuje periodickou reautentizaci, při které může autentizátor během navázaného spojení v náhodných intervalech zasílat nové výzvy, aby zajistil pokračující legitimitu protistrany. Tím se předchází převzetí relace a zajišťuje, že pouze autentizovaná zařízení si udrží síťový přístup.

Implementace CHAP v sítích 3GPP následuje specifické adaptace definované v technických specifikacích, včetně správné integrace s [AAA](/mobilnisite/slovnik/aaa/) (Authentication, Authorization, and Accounting) servery a [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server). Protokol spolupracuje s dalšími bezpečnostními mechanismy, jako je [EAP](/mobilnisite/slovnik/eap/) (Extensible Authentication Protocol), a je často používán jako součást širších autentizačních rámců. Jeho návrh zajišťuje kompatibilitu s různými síťovými architekturami při zachování silných bezpečnostních vlastností prostřednictvím správné správy klíčů a kryptografických operací.

Účinnost protokolu závisí na správné implementaci několika bezpečnostních postupů: použití dostatečně dlouhých a náhodných výzev, zachování důvěrnosti sdílených tajemství, využívání silných hashovacích funkcí a implementace správného zpracování chyb. Jednoduchost a účinnost CHAP z něj učinily základní autentizační mechanismus v telekomunikačních sítích, který poskytuje spolehlivé ověření identity a zároveň minimalizuje vystavení citlivých přihlašovacích údajů během přenosu.

## K čemu slouží

CHAP byl vyvinut k řešení významných bezpečnostních slabin v raných metodách síťové autentizace, zejména těch, které přenášely hesla v čitelné podobě nebo používaly slabou kryptografickou ochranu. Před CHAP autentizační protokoly jako PAP (Password Authentication Protocol) odesílaly přihlašovací údaje bez šifrování, což je činilo náchylnými k odposlechu a replay útokům. Telekomunikační průmysl potřeboval robustnější autentizační mechanismus, který by dokázal chránit před odposloucháváním, útoky typu man-in-the-middle a krádeží přihlašovacích údajů, a zároveň zachovat přiměřenou výpočetní náročnost.

Vznik protokolu byl motivován rostoucí potřebou zabezpečeného vzdáleného přístupu v sítích vytáčeného připojení a vznikajících datových sítích během 90. let 20. století. Jak se telekomunikační sítě vyvíjely z okruhově přepínaných hlasových služeb na paketově přepínané datové služby, riziko neoprávněného přístupu významně vzrostlo. CHAP poskytl standardizovaný způsob autentizace zařízení a uživatelů bez vystavení citlivých informací, využívající kryptografické techniky, které byly výpočetně proveditelné pro hardware té doby. Jeho návrh konkrétně řešil omezení předchozích přístupů odstraněním přenosu hesla a začleněním ochrany proti replay útokům prostřednictvím náhodných výzev.

V systémech 3GPP plní CHAP kritické funkce při zabezpečování mobilních datových spojení, zejména pro služby [GPRS](/mobilnisite/slovnik/gprs/) a následné paketové datové služby. Autentizuje uživatelské zařízení během aktivace PDP kontextu, čímž zajišťuje, že pouze autorizovaná zařízení mohou přistupovat k síťovým zdrojům. Protokol také podporuje roamingové scénáře, kde musí být autentizace provedena napříč doménami různých síťových operátorů. Poskytnutím standardizovaného autentizačního rámce CHAP umožňuje interoperabilitu mezi zařízeními od různých výrobců při zachování konzistentní úrovně zabezpečení napříč různými síťovými nasazeními.

## Klíčové vlastnosti

- Třífázová handshake autentizace bez přenosu hesla
- Mechanismus challenge-response využívající kryptografické hashování
- Podpora periodické reautentizace během navázaných relací
- Generování náhodných výzev k prevenci replay útoků
- Kompatibilita s PPP a různými síťovými architekturami
- Integrace s AAA servery a databázemi účastníků

## Související pojmy

- [EAP – Extensible Authentication Protocol](/mobilnisite/slovnik/eap/)
- [AAA – Authentication, Authorization, and Accounting](/mobilnisite/slovnik/aaa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [CHAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/chap/)
