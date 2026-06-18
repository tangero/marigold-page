---
slug: "usb"
url: "/mobilnisite/slovnik/usb/"
type: "slovnik"
title: "USB – Universal Serial Bus"
date: 2026-01-01
abbr: "USB"
fullName: "Universal Serial Bus"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/usb/"
summary: "USB je standardizované fyzické rozhraní pro připojování zařízení, umožňující přenos dat a napájení. V kontextech 3GPP často odkazuje na použití USB pro připojení zařízení, například pro modemy nebo sd"
---

USB (Universal Serial Bus) je standardizované fyzické rozhraní používané v kontextech 3GPP pro připojení zařízení, například pro modemy nebo sdílení připojení (tethering), umožňující přenos dat a napájení mezi uživatelským zařízením (UE) a externími zařízeními nebo sítěmi.

## Popis

Universal Serial Bus (USB) je průmyslový standard definující kabely, konektory a komunikační protokoly pro propojení, komunikaci a napájení mezi počítači, periferiemi a dalšími zařízeními. Ve specifikacích 3GPP je USB uváděno jako fyzické a linkové rozhraní, které lze využít pro různé účely, například pro připojení uživatelského zařízení (UE) k osobnímu počítači pro sdílení připojení (tethering) nebo pro použití USB adaptéru (dongle) jako modemu pro mobilní širokopásmový přístup. Specifikace podrobně popisují, jak lze USB rozhraní využít pro přenos síťových protokolů a dat, čímž zajišťují interoperabilitu mezi mobilními zařízeními a hostitelskými systémy.

Z architektonického hlediska, když je USB použito v kontextu 3GPP, typicky zahrnuje scénář, kdy UE funguje jako USB zařízení (např. modem) a hostitel (např. notebook) funguje jako USB hostitel. Komunikace přes USB se řídí standardními USB protokoly, přičemž specifikace 3GPP definují, jak jsou síťové protokoly vyšších vrstev, například IP pakety pro datové služby, zapouzdřovány a přenášeny přes toto fyzické médium. To zahrnuje ovladače na straně hostitele, které interpretují USB komunikaci za účelem vytvoření síťového rozhraní, což hostiteli umožňuje využívat síťovou konektivitu UE.

Klíčové komponenty zahrnují fyzický USB konektor (např. Type-A, Type-C), USB řadič uvnitř UE, odpovídající hostitelský řadič a softwarovou vrstvu, která spravuje USB komunikaci a síťové propojení (bridging). Role USB v sítích 3GPP spočívá především v poskytnutí alternativního, standardizovaného drátového rozhraní pro přesměrování dat (data offloading), správu zařízení nebo umožnění funkcí UE, jako jsou mobilní hotspoty. Zajišťuje, že mobilní konektivita může být snadno integrována do široké škály spotřební elektroniky a výpočetních zařízení bez nutnosti proprietárních rozhraní.

Uvedené specifikace, jako jsou TS 23.179 a TS 24.484, pokrývají aspekty jako správa osobní sítě (Personal Network Management – [PNM](/mobilnisite/slovnik/pnm/)) a správa zařízení (Device Management – [DM](/mobilnisite/slovnik/dm/)), kde může být USB použito pro konektivitu mezi zařízeními v osobních sítích ([PAN](/mobilnisite/slovnik/pan/)) nebo pro managementové operace. Tato integrace podtrhuje význam USB jako všudypřítomného rozhraní, které doplňuje bezdrátové technologie při poskytování bezproblémového uživatelského zážitku a flexibilních možností připojení v širším ekosystému připojených zařízení.

## K čemu slouží

USB bylo vytvořeno za účelem standardizace připojování periferií k počítačům, čímž nahradilo množství proprietárních rozhraní jediným univerzálním konektorem. Jeho účelem v ekosystému 3GPP je využít tohoto rozšířeného, spolehlivého a vysokorychlostního rozhraní k usnadnění řešení mobilní konektivity, jako je sdílení připojení (tethering) a vestavěné modemy. Začleněním USB 3GPP zajišťuje, že mobilní zařízení mohou bezproblémově spolupracovat s obrovskou instalovanou základnou počítačů a dalších hostitelů, čímž zvyšuje použitelnost a adopci.

Historicky, předtím než se USB stalo všudypřítomným, mobilní datová konektivita často závisela na sériových portech (jako RS-232) nebo proprietárních kabelech, které byly pomalejší, méně spolehlivé a fragmentované mezi výrobci. Adopce USB ve specifikacích 3GPP tyto nedostatky odstranila poskytnutím standardizovaného vysokokapacitního rozhraní, které podporuje funkci plug-and-play, napájení a robustní přenos dat. Tento vývoj umožnil efektivnější a uživatelsky přívětivější přístup k mobilnímu širokopásmovému připojení a umožnil scénáře, jako je použití chytrého telefonu jako modemu pro notebook pomocí jednoduchého USB kabelu.

Motivace pro zahrnutí USB do standardů 3GPP vychází z potřeby integrovat mobilní telekomunikace se širším odvětvím [IT](/mobilnisite/slovnik/it/) a spotřební elektroniky. Řeší problémy související s kompatibilitou zařízení, snadností použití a výkonem pro drátová datová připojení. Specifikací způsobu použití USB v kontextech, jako je správa zařízení a osobní sítě, 3GPP zajišťuje, že mobilní služby mohou být spolehlivě doručovány přes toto běžné rozhraní, čímž podporuje širokou škálu aplikací od přístupu k internetu až po aktualizace firmwaru.

## Klíčové vlastnosti

- Standardizovaný fyzický konektor zajišťující interoperabilitu mezi zařízeními
- Vysokorychlostní přenos dat podporující rychlosti mobilního širokopásmového připojení
- Funkce plug-and-play pro snadné připojení a konfiguraci
- Napájení přes stejný kabel, umožňující nabíjení zařízení během přenosu dat
- Podpora více datových protokolů zapouzdřených přes USB pro síťový přístup
- Široká adopce ve spotřební elektronice, což snižuje potřebu proprietárních řešení

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance

---

📖 **Anglický originál a plná specifikace:** [USB na 3GPP Explorer](https://3gpp-explorer.com/glossary/usb/)
