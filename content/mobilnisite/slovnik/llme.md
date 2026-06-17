---
slug: "llme"
url: "/mobilnisite/slovnik/llme/"
type: "slovnik"
title: "LLME – Logical Link Management Entity"
date: 2025-01-01
abbr: "LLME"
fullName: "Logical Link Management Entity"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/llme/"
summary: "Logical Link Management Entity (LLME) je funkční entita v architektuře protokolu GPRS, která implementuje procedury správy logického spoje (Logical Link Management, LLM). Nachází se jak v mobilní stan"
---

LLME je funkční entita v architektuře protokolu GPRS, která se nachází jak v mobilní stanici (MS), tak v SGSN a implementuje procedury správy logického spoje (Logical Link Management) pro zřizování, uvolňování a zajištění spolehlivého logického spojení.

## Popis

Logical Link Management Entity (LLME) je implementační komponenta, která vykonává funkce specifikované protokolem správy logického spoje (Logical Link Management, [LLM](/mobilnisite/slovnik/llm/)). Existuje jako softwarový nebo firmware modul v rámci protokolových zásobníků mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) a podpůrného uzlu pro [GPRS](/mobilnisite/slovnik/gprs/) (SGSN). LLME zajišťuje provádění LLM procedur, včetně správy spojů logického spojového řízení (Logical Link Control, [LLC](/mobilnisite/slovnik/llc/)). Zpracovává LLM zprávy, udržuje stavové automaty pro každý logický spoj a interaguje s dalšími entitami, jako je správa mobility GPRS ([GMM](/mobilnisite/slovnik/gmm/)) a správa relace (SM), pro koordinaci aktivit spojů. LLME používá parametry, jako je dočasná identita logického spoje (Temporary Logical Link Identity, TLLI), k identifikaci a správě konkrétních kontextů logických spojů.

Z architektonického hlediska LLME funguje na rozhraní mezi podsložkou LLC a nižšími vrstvami, jako je RLC/[MAC](/mobilnisite/slovnik/mac/). V MS je LLME součástí protokolového zásobníku uživatelského zařízení, zatímco v SGSN je integrována do zpracování na síťové straně. Entita spravuje zřizování spojů iniciováním nebo odpovídáním na požadavky na aktivaci, které zahrnují vyjednávání profilů QoS a alokaci zdrojů. Během přenosu dat LLME dohlíží na údržbu spoje, včetně řízení toku, detekce chyb a dohledu prostřednictvím mechanismů, jako jsou keep-alive signály a obsluha časových limitů. Také zajišťuje procedury uvolňování spojů, což zahrnuje řádné uvolnění zdrojů a informací o kontextu při ukončení relace nebo v důsledku selhání.

Z hlediska fungování LLME spolupracuje s protokolem LLM definovaným v 3GPP TS 44.064. Implementuje stavové přechody a toky zpráv specifikované ve standardu, například převod logického spoje z nečinného stavu do aktivního stavu. LLME podporuje více logických spojů na jednu MS, což umožňuje souběžné datové relace s různými požadavky na QoS. Hraje také roli v mobilních scénářích, pomáhá při opětovném zřizování spojů během předávání mezi buňkami nebo směrovacími oblastmi. Tím, že abstrahuje složitost správy spojů, umožňuje LLME aplikacím vyšších vrstev přenášet data spolehlivě, aniž by se musely zabývat podrobnostmi nízkonákladových spojení, čímž zvyšuje efektivitu sítě a uživatelský zážitek.

## K čemu slouží

Logical Link Management Entity (LLME) byla vytvořena, aby poskytla konkrétní funkční implementaci protokolu správy logického spoje (Logical Link Management, [LLM](/mobilnisite/slovnik/llm/)) v sítích [GPRS](/mobilnisite/slovnik/gprs/) a EGPRS. S vývojem paketově přepínaných mobilních dat vznikla potřeba specializované entity pro efektivní provádění úloh správy spojů, která odděluje funkce řídicí roviny od operací datové roviny. LLME řeší problém správy dynamických logických spojení v prostředí rádiového rozhraní s omezenými zdroji, kde jsou fyzické kanály sdíleny mezi více uživateli. Zajišťuje, že logické spoje jsou řádně zřizovány, udržovány a rušeny, čímž podporuje přerušovanou povahu datového provozu, kterou okruhově přepínané entity nedokázaly efektivně zvládat.

Historicky bylo zavedení LLME ve verzi 8 spolu s LLM motivováno omezeními dřívějších datových služeb GSM, které spoléhaly na jednoduchá bod-bod spojení. Zapouzdřením logiky správy spojů do samostatné entity umožňuje LLME lepší škálovatelnost, zpracování chyb a integraci se správou mobility. Řeší problémy, jako je synchronizace stavu spojů mezi MS a SGSN, efektivní využití zdrojů během nečinných období a obnova po selhání rádiového spoje. Role LLME přetrvává přes mnoho vydání 3GPP díky jejímu zásadnímu významu v paketových jádrových sítích, a to i přesto, že novější technologie, jako jsou LTE a 5G, zavedly odlišné architektury, kde jsou podobné funkce distribuovány napříč jinými protokolovými vrstvami.

## Klíčové vlastnosti

- Implementuje LLM procedury pro řízení logického spoje v MS a SGSN
- Spravuje stavové automaty a kontexty pro více logických spojů
- Zajišťuje operace zřizování, údržby a uvolňování spojů
- Koordinuje se správou mobility (GMM) a správou relace (SM) pro mobilitu a koordinaci relací
- Podporuje vyjednávání QoS a alokaci zdrojů na spoj
- Poskytuje mechanismy detekce chyb a dohledu pro spolehlivost spoje

## Související pojmy

- [LLM – Logical Link Management](/mobilnisite/slovnik/llm/)
- [LLC – SM Low Layer Source Specific Multicast (address)](/mobilnisite/slovnik/llc/)
- [GMM – Global Multimedia Mobility](/mobilnisite/slovnik/gmm/)

## Definující specifikace

- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [LLME na 3GPP Explorer](https://3gpp-explorer.com/glossary/llme/)
