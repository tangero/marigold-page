---
slug: "mgv-f"
url: "/mobilnisite/slovnik/mgv-f/"
type: "slovnik"
title: "MGV-F – MBMS key Generation and Validation Function"
date: 2025-01-01
abbr: "MGV-F"
fullName: "MBMS key Generation and Validation Function"
category: "Security"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/mgv-f/"
summary: "Bezpečnostní funkce v architektuře MBMS (Multimedia Broadcast Multicast Service) odpovědná za generování a distribuci kryptografických klíčů používaných k ochraně vysílaného a multicastovaného obsahu."
---

MGV-F je funkce pro generování a validaci klíčů MBMS (MBMS key Generation and Validation Function), bezpečnostní funkce odpovědná za generování a distribuci kryptografických klíčů pro ochranu vysílaného/multicastovaného obsahu a zajištění, že k němu mají přístup pouze oprávnění účastníci.

## Popis

Funkce pro generování a validaci klíčů [MBMS](/mobilnisite/slovnik/mbms/) (MBMS key Generation and Validation Function, MGV-F) je klíčová bezpečnostní entita definovaná v rámci standardu 3GPP pro službu MBMS (Multimedia Broadcast Multicast Service) počínaje Release 8. Je umístěna v centru služeb MBMS ([BM-SC](/mobilnisite/slovnik/bm-sc/)), což je hlavní síťový prvek, který autorizuje a iniciuje relace MBMS. Primární rolí MGV-F je správa životního cyklu kryptografických klíčů používaných k zabezpečení obsahu MBMS, který je přenášen přes mobilní síť k potenciálně masivním skupinám uživatelů. To zahrnuje generování, ukládání, distribuci a obnovu klíčů, které šifrují vysílaný/multicastovaný provoz ([MTK](/mobilnisite/slovnik/mtk/) - MBMS Traffic Key), a klíčů, které chrání samotné zprávy pro distribuci klíčů ([MSK](/mobilnisite/slovnik/msk/) - MBMS Service Key a [MUK](/mobilnisite/slovnik/muk/) - MBMS User Key).

Z architektonického hlediska MGV-F pracuje ve spojení s úložištěm pro generování a validaci klíčů MBMS ([MGV-S](/mobilnisite/slovnik/mgv-s/)) a s modulem uživatelských služeb (USIM) v uživatelském zařízení (UE). Proces začíná, když se účastník přihlásí k službě MBMS. MGV-F pro tuto dvojici uživatel-sluzba vygeneruje jedinečný uživatelský klíč MBMS (MUK). Pro aktivní relaci MBMS MGV-F vygeneruje relaci specifický klíč provozu MBMS (MTK) používaný k šifrování skutečného mediálního obsahu. Pro bezpečné doručení tohoto MTK autorizovaným uživatelům je zašifrován pomocí služebního klíče MBMS (MSK). MSK a MUK jsou bezpečně zřízeny do USIM uživatele, typicky prostřednictvím stávajícího rámce pro autentizaci a dohodu o klíči UMTS nebo EPS. Zašifrovaný MTK (obalený pomocí MSK) je poté vysílán všem uživatelům v oblasti pokrytí služby. Pouze uživatelé s platným USIM obsahujícím odpovídající MSK mohou MTK dešifrovat a následně dešifrovat vysílaný obsah.

Princip činnosti zahrnuje hierarchickou strukturu klíčů a bezpečné protokoly. MGV-F využívá protokoly architektury pro distribuci klíčů MBMS (MKD). Přijímá žádosti o autorizaci služby, spouští generování klíčů a používá MGV-S jako zabezpečené úložiště pro dlouhodobé klíče, jako jsou MUK a MSK. Pro distribuci klíčů MGV-F instruuje BM-SC, aby vysílal klíčový materiál v řídicím kanálu MBMS. MGV-F také spravuje proceduru obnovy klíčů, která periodicky mění MTK, čímž omezuje dopad případného kompromitování klíče. Celý systém je navržen pro škálovatelnost, protože povaha distribuce klíčů typu point-to-multipoint znamená, že jediná zašifrovaná klíčová zpráva z MGV-F může být použita miliony zařízení současně, na rozdíl od distribuce klíčů point-to-point, která by pro vysílací služby nebyla proveditelná.

## K čemu slouží

MGV-F byla vytvořena, aby řešila základní bezpečnostní výzvu vlastní vysílacím a multicastovým službám: jak efektivně poskytnout důvěrnost obsahu a řízení přístupu velké, dynamické skupině uživatelů přes veřejnou síť. Tradiční bezpečnostní modely pro unicast, jako jsou ty používané pro hlasové hovory nebo prohlížení webu, spoléhají na zabezpečené tunely point-to-point (např. [IPsec](/mobilnisite/slovnik/ipsec/) nebo TLS) vytvořené individuálně s každým uživatelem. Tento model není škálovatelný pro vysílání živé televize nebo softwarových aktualizací milionům zařízení, protože by zahltil síť individuálními vyjednáváními klíčů a šifrovacími datovými toky.

Motivace pro MGV-F vycházela z komerční potřeby zabezpečených prémiových vysílacích služeb, jako je mobilní TV. Operátoři potřebovali způsob, jak monetizovat [MBMS](/mobilnisite/slovnik/mbms/) tím, že zajistí, že placení účastníci mohou dešifrovat obsah, a zabrání tak krádeži služby. MGV-F jako součást standardizovaného bezpečnostního rámce MBMS tuto schopnost poskytla. Vyřešila problém škálovatelné správy klíčů zavedením hierarchického, na skupinu orientovaného systému distribuce klíčů. To umožnilo vysílat jediný šifrovaný provozní datový tok s efektivní distribucí potřebných dešifrovacích klíčů typu point-to-multipoint autorizovaným členům skupiny. Řešila tak omezení předchozích nestandardních nebo chybějících mechanismů zabezpečení vysílání a umožnila nové obchodní modely pro síťové operátory a poskytovatele obsahu v rámci ekosystému 3GPP.

## Klíčové vlastnosti

- Generuje hierarchické klíče MBMS: MUK (uživatelský klíč), MSK (služební klíč) a MTK (provozní klíč)
- Spravuje životní cyklus kryptografických klíčů pro relace MBMS, včetně generování a obnovy
- Je umístěna v BM-SC a komunikuje se zabezpečeným úložištěm (MGV-S)
- Umožňuje škálovatelnou distribuci klíčů typu point-to-multipoint masivním skupinám příjemců
- Poskytuje řízení přístupu, čímž zajišťuje, že obsah mohou dešifrovat pouze autorizovaní účastníci s platným USIM
- Spolupracuje s aplikací USIM pro zabezpečené ukládání a zpracování klíčů v UE

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MGV-S – MBMS key Generation and Validation Storage](/mobilnisite/slovnik/mgv-s/)

## Definující specifikace

- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.246** (Rel-19) — MBMS Security Specification

---

📖 **Anglický originál a plná specifikace:** [MGV-F na 3GPP Explorer](https://3gpp-explorer.com/glossary/mgv-f/)
