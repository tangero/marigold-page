---
slug: "luad"
url: "/mobilnisite/slovnik/luad/"
type: "slovnik"
title: "LUAD – Liberty-Enabled User Agent or Device"
date: 2025-01-01
abbr: "LUAD"
fullName: "Liberty-Enabled User Agent or Device"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/luad/"
summary: "Uživatelský agent nebo zařízení definovaný projektem Liberty Alliance Project (LAP), který podporuje možnosti federované identity a jednotného přihlašování (SSO). Umožňuje zabezpečený přístup ke služb"
---

LUAD (Liberty-Enabled User Agent or Device) je uživatelský agent nebo zařízení definovaný Liberty Alliance, které podporuje federovanou identitu a jednotné přihlašování pro zabezpečený a pohodlný přístup ke službám napříč různými doménami.

## Popis

Liberty-Enabled User Agent or Device (LUAD) je koncept standardizovaný v rámci 3GPP, konkrétně v TS 33.980, který odkazuje na specifikace projektu Liberty Alliance Project ([LAP](/mobilnisite/slovnik/lap/)). LUAD je klientská entita – například mobilní telefon, tablet nebo softwarová aplikace – která implementuje protokoly Liberty Identity Federation Framework ([ID-FF](/mobilnisite/slovnik/id-ff/)). Jejím hlavním účelem je jednat jménem koncového uživatele za účelem usnadnění správy federované identity, což umožňuje bezproblémové a zabezpečené ověřování a autorizaci napříč více poskytovateli služeb bez nutnosti opakovaného zadávání přihlašovacích údajů.

Z architektonického hlediska LUAD komunikuje s několika klíčovými komponentami v ekosystému federované identity. Komunikuje s Poskytovatelem identity (IdP), který uživatele ověří a vydává bezpečnostní tvrzení (assertions), a s Poskytovateli služeb (SP), kteří se na tato tvrzení spoléhají při poskytování přístupu k prostředkům. Samotný LUAD obsahuje softwarové komponenty, které zpracovávají protokolové zprávy, spravují souhlas uživatele a ukládají artefakty federace, jako jsou pseudonymní identifikátory. Podporuje protokoly jako je Liberty Alliance Single Sign-On a Federation protokoly, které jsou často založeny na konstrukcích SAML (Security Assertion Markup Language), což umožňuje interoperabilitu v prostředí více dodavatelů.

Během provozu, když se uživatel pokusí o přístup ke službě u SP, LUAD uživatele přesměruje na jeho určeného IdP, pokud již není ověřen. Po úspěšném ověření IdP vygeneruje bezpečnostní tvrzení obsahující atributy identity a odešle jej zpět LUAD, který jej následně předá SP. SP tvrzení ověří a poskytne přístup. LUAD spravuje celý životní cyklus federace, včetně vytváření okruhů federace (federation circles), šíření požadavků na odhlášení napříč doménami a zpracování správy identifikátorů jmen. Jeho role je klíčová pro abstrakci složitosti správy identit napříč doménami od koncového uživatele a poskytování konzistentního a bezpečného zážitku.

V rámci architektury 3GPP integrace konceptů LUAD podporuje scénáře jako zabezpečený přístup ke službám IP Multimedia Subsystem (IMS) nebo aplikacím třetích stran využívajícím federované identity. Souladí se s širšími bezpečnostními cíli 3GPP pro důvěryhodný přístup a správu identit, zejména v prostředích, kde uživatelé roamují mezi síťovými operátory nebo přistupují ke službám od různých poskytovatelů. Specifikace v TS 33.980 poskytuje pokyny pro implementaci schopností LUAD v sítích 3GPP, zajišťuje kompatibilitu se standardy Liberty Alliance a podporuje jednotný přístup k federaci identit v telekomunikacích.

## K čemu slouží

LUAD byl zaveden pro řešení rostoucí potřeby bezproblémové a bezpečné správy identit napříč různými doménami služeb, což je výzva umocněná rozšířením mobilních internetových služeb a ekosystémů s více poskytovateli. Před jeho přijetím uživatelé často čelili nutnosti udržovat samostatné přihlašovací údaje pro každou službu, což vedlo ke špatné uživatelské zkušenosti, únavě z hesel a zvýšeným bezpečnostním rizikům způsobeným opakovaným používáním přihlašovacích údajů. Projekt Liberty Alliance Project, průmyslové konsorcium, vyvinul frameworky pro umožnění federované identity, které uživatelům umožňují ověřit se jednou a přistupovat k více službám. 3GPP tyto koncepty začlenilo, aby zvýšilo dostupnost a bezpečnost služeb v mobilních sítích.

Motivace pro standardizaci LUAD v rámci 3GPP vycházela z touhy využít federovanou identitu pro telekomunikační služby, jako jsou aplikace založené na IMS, mobilní obchod a partnerské služby. Definováním Liberty-podporujícího zařízení (Liberty-enabled device) zajistilo 3GPP, že mobilní zařízení mohou nativně podporovat protokoly pro federaci identit, což operátorům umožňuje nabízet služby s přidanou hodnotou s možnostmi jednotného přihlašování. Tato integrace řešila omezení dřívějších izolovaných metod ověřování, které byly neefektivní pro roamující uživatele nebo přístup napříč službami, a souladila se trendy směřujícími ke konvergenci telekomunikačních a internetových služeb.

Historicky, jak se sítě 3GPP vyvíjely směrem k architekturám plně založeným na IP a bohatší nabídce služeb, stala se správa uživatelských identit napříč různými administrativními doménami kritickou. LUAD poskytl standardizovaný způsob implementace klientů pro federovanou identitu, usnadňující interoperabilitu mezi mobilními síťovými operátory, poskytovateli aplikací a poskytovateli identit. Řešil problémy uživatelského komfortu, snížil režii spojenou s ověřováním a zvýšil bezpečnost prostřednictvím centralizované správy identit, čímž podpořil obchodní modely spoléhající se na důvěryhodná partnerství a bezproblémové poskytování služeb.

## Klíčové vlastnosti

- Podporuje protokoly Liberty Alliance Identity Federation Framework (ID-FF)
- Umožňuje jednotné přihlašování (SSO) napříč více poskytovateli služeb
- Spravuje životní cyklus federované identity včetně vytvoření a ukončení
- Zpracovává bezpečnostní tvrzení (security assertions) a správu pseudonymních identifikátorů
- Integruje se s bezpečnostní architekturou 3GPP pro důvěryhodný přístup
- Usnadňuje souhlas uživatele a kontrolu soukromí při ověřování napříč doménami

## Definující specifikace

- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [LUAD na 3GPP Explorer](https://3gpp-explorer.com/glossary/luad/)
