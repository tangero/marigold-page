---
slug: "kakma"
url: "/mobilnisite/slovnik/kakma/"
type: "slovnik"
title: "KAKMA – AKMA Anchor Key"
date: 2025-01-01
abbr: "KAKMA"
fullName: "AKMA Anchor Key"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/kakma/"
summary: "Kořenový, dlouhodobý symetrický klíč v rámci AKMA, vygenerovaný z autentizace v 5G core síti. Slouží jako hlavní tajemství, ze kterého se odvozují aplikačně specifické klíče (KAF), a kotví bezpečnost"
---

KAKMA je kořenový symetrický klíč v rámci AKMA, vygenerovaný z 5G autentizace, který slouží jako hlavní tajemství pro odvozování aplikačně specifických klíčů a kotví bezpečnost aplikací k síťovým přihlašovacím údajům účastníka.

## Popis

KAKMA ([AKMA](/mobilnisite/slovnik/akma/) Anchor Key) je základní kryptografický klíč v systému Authentication and Key Management for Applications (AKMA). Jedná se o symetrický klíč vytvořený jako vedlejší produkt úspěšného primárního autentizačního procesu mezi uživatelským zařízením (UE) a 5G Core sítí, konkrétně pomocí protokolů 5G [AKA](/mobilnisite/slovnik/aka/) nebo EAP-AKA'. Během této autentizace klíč KAKMA generuje funkce Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)). Následně je bezpečně uložen a spravován specializovanou síťovou funkcí zvanou AKMA Anchor Function (AAnF) v domovské síti účastníka. Odpovídající klíč KAKMA je také nezávisle odvozen v UE za použití jeho uložených přihlašovacích údajů a autentizačních parametrů přijatých ze sítě.

Klíč KAKMA se nepoužívá přímo k zabezpečení žádného provozu. Jeho jediným účelem je sloužit jako kořenový klíč pro odvozování dalších klíčů, především AKMA Application Keys ([KAF](/mobilnisite/slovnik/kaf/)). K odvození KAF z KAKMA se používá funkce pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)) se specifickými vstupními parametry, včetně identity cílové Application Function. Tím je zajištěno kryptografické oddělení: každá aplikace získá unikátní klíč odvozený ze stejného kořene, což zabrání tomu, aby kompromitace jedné aplikace ovlivnila ostatní. AAnF na straně sítě působí jako správce klíče KAKMA a používá jej k vytváření klíčů KAF na požádání pro autorizované Application Functions.

Z architektonického hlediska je KAKMA jádrem modelu důvěry AKMA. Spojuje svět zabezpečení síťového přístupu (zajišťovaného [AMF](/mobilnisite/slovnik/amf/), AUSF a [UDM](/mobilnisite/slovnik/udm/)) a zabezpečení na aplikační úrovni. Jeho životní cyklus je řízen sítí a je typicky platný po dobu registračního stavu UE nebo po konfigurované časové období. Když se UE odregistruje nebo platnost klíče vyprší, je KAKMA smazán, čímž se zneplatní všechny z něj odvozené klíče KAF, a poskytuje se tak centralizovaná bezpečnostní kontrola. Bezpečnost celého rámce AKMA závisí na důvěrnosti a integritě klíče KAKMA, který je chráněn v bezpečném prostředí odolného proti neoprávněné manipulaci prvku v UE a důvěryhodných funkcí domovské sítě.

## K čemu slouží

KAKMA byl vytvořen za účelem poskytnutí trvalé kryptografické kotvy odvozené ze sítě, která rozšiřuje důvěru z primární 3GPP autentizace do aplikační vrstvy. Před zavedením [AKMA](/mobilnisite/slovnik/akma/) neexistoval standardizovaný mechanismus, který by aplikacím umožňoval využít silnou SIM-based autentizaci mobilní sítě. Aplikace musely od nuly vytvářet svůj vlastní bezpečnostní kontext, často pomocí slabších metod. KAKMA tento problém řeší vytvořením opakovaně použitelného bezpečnostního aktiva po síťové autentizaci.

Jeho existence řeší problém autentizačních izolovaných systémů. Bez něj by si každý poskytovatel služeb (Application Function) musel implementovat vlastní autentizaci a dohodu o klíči s uživatelem, což by vedlo k roztříštěné uživatelské zkušenosti a složitému řízení klíčů. KAKMA poskytuje společný kořen důvěry v rámci domény domovského operátora, což umožňuje více, potenciálně nesouvisejícím Application Functions získat bezpečné, uživatelsky specifické klíče, aniž by se přímo dostaly do styku s dlouhodobými přihlašovacími údaji uživatele.

Motivace je zakořeněna v umožnění nových paradigmat služeb, jako je bezpečné připojování IoT zařízení, bezproblémový přístup k mediálním službám a federace identit, kde je identita mobilní sítě cenným aktivem. Zavedením KAKMA definoval 3GPP standardizovaný způsob inicializace širokého spektra bezpečnostních relací aplikací, což zjednodušuje vývoj pro poskytovatele služeb a zvyšuje bezpečnost a použitelnost pro koncové uživatele. Přeměňuje síť z pouhého poskytovatele konektivity na důvěryhodnou bezpečnostní kotvu pro digitální ekosystém.

## Klíčové vlastnosti

- Generován jednou při každé úspěšné primární síťové autentizaci (5G AKA/EAP-AKA').
- Slouží jako kořenový klíč pro odvozování všech AKMA Application Keys (KAFs).
- Bezpečně uložen v AKMA Anchor Function (AAnF) v domovské síti a v UE.
- Má životní cyklus vázaný na registraci UE, což poskytuje centralizované zneplatnění.
- Nikdy není vystaven Application Functions, čímž chrání kořen hierarchie klíčů.
- Umožňuje kryptografické oddělení pro různé aplikace prostřednictvím odvozování klíčů s unikátními vstupy.

## Související pojmy

- [AKMA – Authentication and Key Management for Applications](/mobilnisite/slovnik/akma/)
- [KAF – AKMA Application Key](/mobilnisite/slovnik/kaf/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)

## Definující specifikace

- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.535** (Rel-19) — 5G AKMA: Authentication and Key Management for Apps

---

📖 **Anglický originál a plná specifikace:** [KAKMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/kakma/)
