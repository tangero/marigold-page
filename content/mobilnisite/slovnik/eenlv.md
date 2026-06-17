---
slug: "eenlv"
url: "/mobilnisite/slovnik/eenlv/"
type: "slovnik"
title: "EENLV – Extended Emergency Number List Validity"
date: 2025-01-01
abbr: "EENLV"
fullName: "Extended Emergency Number List Validity"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/eenlv/"
summary: "Funkce prodlužující platnost seznamu nouzových čísel uloženého v UE. Zajišťuje, že UE může přistupovat k nouzovým službám, i když nemůže kontaktovat síť pro obnovení seznamu, čímž zvyšuje spolehlivost"
---

EENLV je funkce, která prodlužuje platnost seznamu nouzových čísel uloženého v zařízení, aby bylo zajištěno přístup k nouzovým službám, když síť není dostupná pro jeho obnovení.

## Popis

Extended Emergency Number List Validity (EENLV) je funkce definovaná ve specifikacích 3GPP, která spravuje interní vyrovnávací paměť (cache) čísel nouzových služeb v UE (User Equipment). UE typicky přijímá 'Emergency Number List' od sítě prostřednictvím signalizace [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum), který obsahuje volací kódy (např. 112, 911, 999) platné v její aktuální lokalitě nebo registrované PLMN. Tento seznam má omezený časovač platnosti. EENLV rozšiřuje operační logiku tohoto časovače, aby zajistila, že UE může stále provést pokus o nouzové volání pomocí potenciálně zastaralého seznamu, pokud se nemůže dostat k síti pro získání nového.

Z architektonického hlediska je EENLV implementována v rámci vrstvy NAS v UE, konkrétně v podsložkách Mobility Management ([MM](/mobilnisite/slovnik/mm/)) a Connection Management ([CM](/mobilnisite/slovnik/cm/)), které zpracovávají registraci účastníka a správu relací. Funkce interaguje s interním úložištěm UE (často aplikace USIM nebo zabezpečená paměť), kde je uložen naposledy přijatý Emergency Number List a jeho přidružený časovač platnosti. Jádrová síť udává dobu platnosti seznamu, ale s EENLV UE uplatňuje rozšířená pravidla pro použití vypršeného seznamu.

Operačně, když UE potřebuje uskutečnit nouzové volání, nejprve zkontroluje svůj uložený Emergency Number List. Pokud časovač platnosti seznamu vypršel, standardní chování by mohlo pokus o volání znemožnit. S povolenou funkcí EENLV je UE za specifických podmínek povoleno použít vypršený seznam, primárně když je ve stavu, ve kterém nemůže úspěšně provést registraci nebo aktualizaci polohy pro získání nového seznamu – například v omezeném stavu služeb (např. mimo dosah domovské sítě, ale v dosahu jakékoli dostupné buňky). UE použije poslední známý platný seznam k interpretaci vytočených číslic.

Tento mechanismus je klíčový pro záložní logiku UE. Zajišťuje, že přístup k nouzovým službám orientovaný na člověka má přednost před striktním dodržováním protokolových časovačů. Síť může řídit parametry funkce, ale autonomní rozhodování UE během scénářů selhání je posíleno. EENLV nemění procedury na straně sítě; jde o zlepšení spolehlivosti na straně UE pro zjišťování nouzových služeb.

## K čemu slouží

EENLV byla zavedena, aby vyřešila kritickou mezeru ve spolehlivosti nouzového volání. Před jejím zavedením, pokud uložený Emergency Number List v UE vypršel a UE nemohla kontaktovat síť pro jeho obnovení (např. z důvodu nedostupného pokrytí, stavu rádiového selhání nebo nepovolené PLMN), UE nemusela rozpoznat vytočené nouzové číslo. To mohlo znemožnit celý pokus o nouzové volání, což vytvářelo nebezpečný scénář, kdy uživatel v nouzi nemůže ani pokusit se připojit k jakémukoli dostupnému rádiovému přístupu.

Historický kontext spočívá ve vzrůstající závislosti na konfiguraci poskytované sítí pro služby, včetně nouzových čísel, která se liší podle země a regionu. Zatímco tato dynamika je prospěšná, zavedla závislost: UE bez nedávného kontaktu se sítí mohla mít neplatný přehled nouzových kódů. EENLV to řeší tím, že umožňuje UE použít svou poslední známou konfiguraci jako záložní řešení typu 'best-effort', upřednostňujíc schopnost pokusit se o volání před jistotou platnosti čísla. To je v souladu s regulačními a bezpečnostními principy, že nouzový přístup by měl být maximálně dostupný.

Funkce zmírňuje omezení striktně časovačem řízeného přístupu. Bere v úvahu, že v mnoha nouzových scénářích může být lokalita uživatele nebo síťové podmínky narušeny. Rozšířením logiky platnosti snižuje riziko falešně negativního výsledku, kdy UE nesprávně rozhodne, že nouzové číslo je neplatné. Doplnuje další funkce spolehlivosti, jako je podpora nouzových volání v omezeném stavu služeb a nouzové služby přenosu.

## Klíčové vlastnosti

- Prodlužuje použitelnost vypršeného Emergency Number List uloženého v UE
- Spouští záložní chování, když je UE v omezeném stavu služeb nebo nemůže kontaktovat síť
- Autonomní provoz na straně UE bez nutnosti interakce se sítí pro toto rozhodnutí
- Udržuje soulad s regulačními požadavky na dostupnost nouzových služeb
- Konfigurovatelná pomocí parametrů poskytovaných sítí, ale s bezpečnostní logikou implementovanou v UE
- Integruje se s NAS procedurami pro správu mobility a zřizování nouzových volání

## Definující specifikace

- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System

---

📖 **Anglický originál a plná specifikace:** [EENLV na 3GPP Explorer](https://3gpp-explorer.com/glossary/eenlv/)
