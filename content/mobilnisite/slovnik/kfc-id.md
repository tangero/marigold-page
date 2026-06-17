---
slug: "kfc-id"
url: "/mobilnisite/slovnik/kfc-id/"
type: "slovnik"
title: "KFC-ID – Key for Floor Control Identifier"
date: 2026-01-01
abbr: "KFC-ID"
fullName: "Key for Floor Control Identifier"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/kfc-id/"
summary: "Kryptografický klíč používaný k zabezpečení zpráv řízení přístupu k médiím (floor control) ve službách Mission Critical Push-to-Talk (MCPTT). Zajišťuje, že pouze autorizovaní uživatelé mohou v skupino"
---

KFC-ID je kryptografický klíč, který zabezpečuje zprávy řízení přístupu k médiím (floor control) v službách MCPTT, aby bylo zajištěno, že pouze oprávnění uživatelé mohou žádat nebo být pověřeni oprávněním mluvit.

## Popis

Key for Floor Control Identifier (KFC-ID) je bezpečnostní klíč definovaný v rámci standardů 3GPP pro služby Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), konkrétně pro Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Jeho primární funkcí je chránit integritu a důvěrnost signalizace řízení přístupu k médiím (floor control). Řízení přístupu k médiím je mechanismus, který rozhoduje, který uživatel ve skupinové komunikační relaci má právo v daném okamžiku přenášet média (tj. mluvit). KFC-ID se používá k odvození dalších klíčů, jako jsou klíče KFCenc a KFCint, které se následně použijí k šifrování a ochraně integrity zpráv řízení přístupu k médiím vyměňovaných mezi klientem MCPTT a serverem MCPTT. Tyto zprávy zahrnují žádosti o přístup, udělení přístupu, zamítnutí přístupu a uvolnění přístupu.

Z architektonického hlediska je KFC-ID zřízen jako součást klíčového materiálu v bezpečnostním kontextu uživatele MCPTT. Typicky je odvozen z kořenového klíče, jako je klíč Kmcptt, pomocí funkce pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)) se specifickými vstupními parametry, které zahrnují identifikátor služby MCPTT a další vazební data, aby bylo zajištěno oddělení klíčů. Proces odvozování zajišťuje, že KFC-ID je jedinečný pro uživatele a konkrétní instanci služby MCPTT. Správu tohoto klíče zajišťuje služba správy klíčů ([KMS](/mobilnisite/slovnik/kms/)) nebo související bezpečnostní funkce v architektuře MCPTT.

Během provozu, když klient MCPTT potřebuje odeslat zprávu řízení přístupu k médiím, příslušná bezpečnostní vrstva použije klíče odvozené z KFC-ID k vytvoření zabezpečeného přenosu. Pro integritu se vypočítá a připojí kód pro ověření zprávy ([MAC](/mobilnisite/slovnik/mac/)). Pro důvěrnost může být zpráva zašifrována. Přijímající entita (server MCPTT nebo jiný klient, v závislosti na režimu komunikace) použije své odpovídající klíče odvozené z KFC-ID k ověření integrity a dešifrování zprávy. Tento proces je zásadní ve vysoce rizikových prostředích, jako je veřejná bezpečnost, kde zajištění, že pouze legitimní, autorizovaný personál může ovládat přístup k médiím, zabraňuje chaosu, podvržení a útokům typu odepření služby na kanálu pro mluvení.

Jeho role přesahuje základní ochranu; je to základní prvek pro zabezpečenou správu skupin a dynamickou identifikaci mluvčího. Díky kryptografickému propojení příkazů řízení přístupu k médiím s identitou uživatele a kontextem relace umožňuje KFC-ID bezpečně implementovat funkce jako prioritní žádosti o přístup (např. nouzové přerušení). Bez tohoto klíče by signalizace řízení přístupu k médiím byla zranitelná, což by umožnilo škodlivým aktérům zmocnit se přístupu, blokovat legitimní uživatele nebo narušovat koordinované nouzové zásahy. KFC-ID je tedy specializovaný klíč v rámci bezpečnostní hierarchie 3GPP MCPTT určený k zabezpečení mechanismu rozhodování v reálném čase, který je klíčový pro efektivní skupinovou komunikaci push-to-talk.

## K čemu slouží

KFC-ID byl zaveden, aby řešil specifické bezpečnostní slabiny v protokolu řízení přístupu k médiím (floor control) služeb Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Před jeho standardizací systémy push-to-talk, zejména ty používané v oblasti veřejné bezpečnosti a kritických komunikací, často spoléhaly na proprietární nebo méně bezpečné mechanismy pro rozhodování o přístupu k médiím. To je činilo náchylnými k útokům, jako je zmocnění se přístupu k médiím, kdy neoprávněný uživatel mohl vysílat do skupiny, nebo odposlechu signalizace, který mohl odhalit operační postupy. Potřeba standardizovaného, robustního bezpečnostního rámce se stala prvořadou, když 3GPP vyvíjelo LTE a 5G pro podporu služeb pro kritické mise, které vyžadují komerční úroveň zabezpečení pro životně důležité operace.

Vytvoření KFC-ID bylo motivováno požadavkem na oddělení kryptografických klíčů podle bezpečnostní funkce – princip známý jako oddělení klíčů. V širší bezpečnostní architektuře MCPTT chrání různé klíče různé aspekty: ověřování uživatele, šifrování médií a signalizaci. Signalizace řízení přístupu k médiím, jakožto samostatná a kritická signalizační rovina, vyžadovala vlastní vyhrazený klíčový materiál, aby se zabránilo tomu, že ohrožení v jedné oblasti (např. přenos médií) ovlivní jinou oblast (řízení přístupu k médiím). Tato izolace zvyšuje celkovou odolnost systému. KFC-ID poskytuje tento vyhrazený kořen pro zabezpečení řízení přístupu k médiím.

Jeho zavedení v 3GPP Release 14 navíc časově souviselo se zráním specifikací MCPTT, což umožnilo interoperabilitu mezi zařízeními různých výrobců při zachování vysoké bezpečnosti. Vyřešil problém, jak bezpečně implementovat dynamické řízení přístupu k médiím s nízkou latencí v IP síti, která může být potenciálně nezabezpečená. Definováním specifického klíče pro tento účel zajistil 3GPP, že zprávy řízení přístupu k médiím mohou být chráněny z hlediska integrity a volitelně šifrovány, čímž splnil přísné požadavky orgánů veřejné bezpečnosti na bezpečnou a spolehlivou skupinovou komunikaci. Odstranil tak omezení starších systémů, kterým buď taková podrobná bezpečnost chyběla, nebo ji implementovaly ad-hoc, neinteroperabilním způsobem.

## Klíčové vlastnosti

- Vyhrazený kryptografický klíč pro zabezpečení signalizace řízení přístupu k médiím (floor control)
- Používá se k odvození samostatných klíčů pro šifrování (KFCenc) a integritu (KFCint)
- Zajišťuje integritu a důvěrnost zpráv žádosti o přístup, udělení přístupu a uvolnění přístupu k médiím
- Podporuje princip oddělení klíčů v rámci bezpečnostní hierarchie MCPTT
- Umožňuje bezpečnou implementaci prioritního řízení přístupu k médiím (např. nouzové přerušení)
- Zřizován a spravován v rámci bezpečnostního kontextu uživatele MCPTT, obvykle prostřednictvím služby správy klíčů (KMS)

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service

---

📖 **Anglický originál a plná specifikace:** [KFC-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/kfc-id/)
