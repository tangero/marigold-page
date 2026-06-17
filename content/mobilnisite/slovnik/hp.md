---
slug: "hp"
url: "/mobilnisite/slovnik/hp/"
type: "slovnik"
title: "HP – Hosting Party"
date: 2025-01-01
abbr: "HP"
fullName: "Hosting Party"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/hp/"
summary: "Hosting Party (HP) je logická entita definovaná v 3GPP pro scénáře bezpečného hostování a delegace služeb, zejména pro služby založené na blízkosti (ProSe). Funguje jako důvěryhodný zprostředkovatel,"
---

HP je logická entita v 3GPP, která funguje jako důvěryhodný zprostředkovatel pro bezpečné hostování aplikací nebo funkcí jménem poskytovatele služeb, zejména pro služby založené na blízkosti (ProSe).

## Popis

Hosting Party (HP) je funkční role v rámci bezpečnostní architektury 3GPP, specifikovaná primárně pro služby založené na blízkosti (ProSe) a později pro komunikaci vozidlo-se-vším (V2X). Nejde o fyzický síťový prvek, ale o logickou entitu, která se účastní procesů autentizace a autorizace. HP typicky sídlí mimo jádrovou síť operátora 3GPP, ale je jí důvěřována prostřednictvím definovaných bezpečnostních asociací a procedur. Její hlavní rolí je hostovat aplikace nebo servisní logiku, jako je ProSe Application Server nebo V2X Application Server, a jednat jménem skutečného poskytovatele služeb nebo uživatelského zařízení (UE) v bezpečnostních výměnách.

Architektonicky HP komunikuje se sítí 3GPP prostřednictvím standardizovaných referenčních bodů, nejvýznamněji s funkcí ProSe v jádrové síti. Bezpečnostní procedury zahrnují autentizaci HP vůči síti 3GPP, často za použití přihlašovacích údajů poskytnutých síťovým operátorem nebo důvěryhodnou třetí stranou. Po autentizaci může HP žádat o autorizaci pro konkrétní služby, jako je povolení přímé komunikace mezi zařízeními pro skupinu uživatelů nebo správa skupinové komunikace pro scénáře V2X. Funkce ProSe v síti 3GPP tyto žádosti ověřuje vůči uživatelským předplatným a politikám.

Provoz HP se řídí bezpečnostním rámcem, který zajišťuje legitimitu služeb a chrání síťové prostředky. Klíčovými komponentami v této interakci jsou přihlašovací údaje HP (jako certifikáty), autorizační schopnosti serveru funkce ProSe a podkladové autentizační mechanismy (např. založené na variantách [AKA](/mobilnisite/slovnik/aka/)). HP může být také zapojena do správy klíčů a napomáhat při bezpečné distribuci klíčů používaných pro šifrování nebo ochranu integrity přímé komunikace mezi zařízeními. Tento model delegace umožňuje specializovaným poskytovatelům služeb využít autentizaci 3GPP a důvěru sítě, aniž by museli budovat vlastní infrastrukturu pro mobilní autentizaci od nuly.

## K čemu slouží

Koncept Hosting Party byl zaveden, aby řešil potřebu bezpečného a delegovaného hostování služeb v nově vznikajících servisních architekturách 3GPP, počínaje službami založenými na blízkosti (ProSe) v Release 9. Předtím byly služby typicky buď plně hostované operátorem v jádrové síti, nebo zcela externí s omezenou integrací důvěry. To vytvářelo mezeru pro poskytovatele služeb třetích stran, kteří chtěli nabízet služby vyžadující těsnou integraci s autentizací, mobilitou a řízením politik 3GPP – například přímou komunikaci mezi zařízeními pro veřejnou bezpečnost nebo sociální aplikace.

Model HP tento problém řeší definováním role důvěryhodného zprostředkovatele, kterého může autorizovat síťový operátor. Umožňuje rozdělení odpovědnosti, kdy operátor spravuje podkladovou autentizaci účastníka a přístup k síti, zatímco HP spravuje aplikační servisní logiku a zapojení uživatelů. To je zvláště kritické pro ProSe a V2X, kde musí být přímá komunikace s nízkou latencí bezpečně autorizována a monitorována. Rámec HP poskytuje standardizovaný způsob, jak tuto důvěru navázat, čímž předchází proprietárním řešením a zajišťuje interoperabilitu mezi různými operátory a poskytovateli služeb. Řízeným způsobem rozšiřuje bezpečnostní perimetr 3GPP, což usnadňuje inovace služeb bez kompromisů v síťové bezpečnosti.

## Klíčové vlastnosti

- Funguje jako logická důvěryhodná entita mimo jádrovou síť 3GPP
- Integruje se s funkcí ProSe pro autentizaci a autorizaci
- Podporuje hostování ProSe Application Server a V2X Application Server
- Účastní se správy bezpečnostních klíčů pro služby přímé komunikace
- Umožňuje delegovanou správu služeb pro poskytovatele třetích stran
- Využívá bezpečnostní přihlašovací údaje a procedury definované v 3GPP

## Definující specifikace

- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TS 33.545** (Rel-19) — Security for NR Femto Subsystem

---

📖 **Anglický originál a plná specifikace:** [HP na 3GPP Explorer](https://3gpp-explorer.com/glossary/hp/)
