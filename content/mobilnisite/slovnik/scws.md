---
slug: "scws"
url: "/mobilnisite/slovnik/scws/"
type: "slovnik"
title: "SCWS – Smart Card Web Server"
date: 2025-01-01
abbr: "SCWS"
fullName: "Smart Card Web Server"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/scws/"
summary: "Webový server běžící na UICC (SIM kartě), který umožňuje zabezpečené dálkové (OTA) zřizování a správu aplikací a dat. Umožňuje síťovým operátorům a poskytovatelům služeb komunikovat přímo s UICC prost"
---

SCWS je webový server běžící na UICC (SIM kartě), který umožňuje zabezpečené dálkové (over-the-air) zřizování a správu aplikací, což síťovým operátorům umožňuje komunikovat přímo s kartou prostřednictvím HTTP/HTTPS.

## Popis

Smart Card Web Server (SCWS) je funkční komponenta vestavěná do UICC (Universal Integrated Circuit Card), jako je [SIM](/mobilnisite/slovnik/sim/), [USIM](/mobilnisite/slovnik/usim/) nebo [ISIM](/mobilnisite/slovnik/isim/). Implementuje odlehčený [HTTP](/mobilnisite/slovnik/http/)/[HTTPS](/mobilnisite/slovnik/https/) serverový stack, což umožňuje UICC hostovat webové stránky a aplikace. Externí entity, jako je prohlížeč mobilního zařízení (fungující jako HTTP klient) nebo vzdálená [OTA](/mobilnisite/slovnik/ota/) (Over-The-Air) platforma, mohou navázat zabezpečené spojení se SCWS pomocí standardních webových protokolů. Komunikace obvykle probíhá přes Bearer Independent Protocol (BIP), který poskytuje datový kanál mezi terminálem a UICC. SCWS spravuje lokální souborový systém na UICC obsahující webové zdroje ([HTML](/mobilnisite/slovnik/html/), obrázky, skripty) a může provádět logiku na straně serveru (např. přes S@T, Javacard). To umožňuje interaktivní uživatelská rozhraní poskytovaná přímo ze SIM karty, přístupná z prohlížeče mobilního zařízení. Pro vzdálenou OTA správu se může k SCWS připojit vyhrazená OTA platforma pomocí HTTPS, aby bezpečně instalovala, aktualizovala nebo mazala aplikace a soubory na UICC. SCWS funguje jako brána, která interpretuje HTTP požadavky, přistupuje k souborovému systému nebo apletu UICC a vrací odpovídající HTTP odpovědi, čímž propojuje webové technologie s bezpečným a proti manipulaci chráněným prostředím čipové karty.

## K čemu slouží

SCWS byl vyvinut za účelem modernizace a zjednodušení správy aplikací a služeb na UICC. Před zavedením SCWS se dálkové zřizování ([OTA](/mobilnisite/slovnik/ota/)) často spoléhalo na proprietární, binární protokoly založené na SMS, které byly složité a měly omezenou funkčnost. Růst mobilních datových služeb a potřeba dynamického zřizování služeb vyžadovaly flexibilnější, standardizovaný přístup. Vestavbou webového serveru do UICC využívá SCWS všudypřítomné webové standardy (HTTP/HTTPS) k vytvoření univerzálního rozhraní pro správu služeb. To umožňuje operátorům vzdáleně nasazovat a aktualizovat přidané služby (jako mobilní bankovnictví, věrnostní programy nebo zabezpečené úložiště) bez nutnosti fyzické výměny karty. Také umožňuje vytváření bohatých, v prohlížeči přístupných rozhraní hostovaných přímo na zabezpečeném prvku, což zlepšuje uživatelský zážitek a bezpečnost aplikací založených na SIM. Jeho zavedení ve 3GPP Release 8 bylo klíčovým krokem v přeměně UICC ze statického autentizačního modulu na dynamickou platformu pro poskytování služeb.

## Klíčové vlastnosti

- HTTP/HTTPS server vestavěný do UICC (SIM/USIM/ISIM)
- Umožňuje vzdálenou OTA správu aplikací a souborů na UICC prostřednictvím webových protokolů
- Hostuje webové stránky a aplikace lokálně na čipové kartě
- Používá Bearer Independent Protocol (BIP) pro přenos dat mezi terminálem a UICC
- Poskytuje zabezpečené, standardizované rozhraní pro zřizování služeb
- Usnadňuje interakci s uživatelem prostřednictvím prohlížeče v zařízení přistupujícího k obsahu hostovanému na kartě

## Definující specifikace

- **TS 31.220** (Rel-19) — Contact Manager for UICC Applications

---

📖 **Anglický originál a plná specifikace:** [SCWS na 3GPP Explorer](https://3gpp-explorer.com/glossary/scws/)
