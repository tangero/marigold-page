---
slug: "dn-aaa"
url: "/mobilnisite/slovnik/dn-aaa/"
type: "slovnik"
title: "DN-AAA – Data Network Authentication, Authorization and Accounting"
date: 2025-01-01
abbr: "DN-AAA"
fullName: "Data Network Authentication, Authorization and Accounting"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dn-aaa/"
summary: "Funkční entita v rámci 5G Core Network, která poskytuje služby autentizace, autorizace a účtování specificky pro připojení uživatele k externí datové síti (DN). Umožňuje operátorovi DN řídit a sledova"
---

DN-AAA je entita 5G Core Network, která poskytuje služby autentizace, autorizace a účtování (Authentication, Authorization, and Accounting) specificky pro připojení uživatele k externí datové síti.

## Popis

DN-AAA je logická funkce definovaná v architektuře 5G System (5GS), která se nachází uvnitř nebo rozhraní s externí datovou sítí ([DN](/mobilnisite/slovnik/dn/)). Jejím hlavním úkolem je provádět [AAA](/mobilnisite/slovnik/aaa/) procedury pro User Equipment (UE) přistupující ke službám v této DN. Funguje ve spolupráci, ale odděleně od funkcí AAA 3GPP, které pro přístup k core síti vykonávají Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) a Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)). DN-AAA komunikuje s 5G Core Network přes Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) nebo přímo se Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v závislosti na scénáři nasazení.

Jak to funguje, zahrnuje několik kroků. Když UE naváže [PDU](/mobilnisite/slovnik/pdu/) Session k DN, která vyžaduje externí AAA, SMF může spustit autentizaci/autorizaci specifickou pro DN. SMF může komunikovat se serverem DN-AAA, typicky pomocí protokolu Diameter nebo [RADIUS](/mobilnisite/slovnik/radius/) přes rozhraní N6 nebo přes NEF, pokud je DN-AAA služba třetí strany. Server DN-AAA autentizuje uživatele (často pomocí přihlašovacích údajů oddělených od předplatného 3GPP), autorizuje konkrétní službu nebo QoS profil a může zahájit účtování datové relace. Výsledek autorizace (např. povolená QoS, limity délky relace) je předán zpět SMF, která tato pravidla vynucuje v rámci 3GPP sítě pro danou PDU Session.

Klíčové komponenty zahrnují samotný server DN-AAA, který uchovává uživatelské profily a politiky pro DN, a standardizovaná rozhraní k 5G Core. Jeho role je klíčová pro umožnění podnikům a poskytovatelům služeb třetích stran integrovat jejich stávající AAA infrastrukturu se sítěmi 5G bez nutnosti přímého přístupu k 3GPP HSS/UDM. To umožňuje flexibilní obchodní modely, například když podnik spravuje přístup ke své firemní síti pro uživatele 5G, zatímco mobilní operátor spravuje přístup k rádiové a core síti odděleně.

## K čemu slouží

DN-AAA bylo zavedeno v 5G k řešení potřeby bezproblémové a bezpečné integrace externích datových sítí (jako podnikové sítě, IoT platformy nebo internetové služby) se systémem 5G. Předchozí generace postrádaly standardizovanou, síti vystavenou metodu, aby datová síť mohla provádět vlastní AAA, což často vedlo k neohrabaným řešením nebo vyžadovalo, aby operátor 3GPP spravoval všechny přihlašovací údaje jménem operátora DN.

Jeho vznik byl motivován vizí 5G v oblasti vystavení síťových funkcí a podpory vertikálních odvětví. Podniky požadují kontrolu nad tím, kdo a jak přistupuje k jejich zdrojům, využívajíce své stávající systémy správy identit a přístupu. DN-AAA to řeší tím, že poskytuje čistý, standardizovaný bod v procesu navazování PDU Session, kde lze vyvolat AAA politiku externí sítě. Toto oddělení kompetencí je zásadní: mobilní operátor autentizuje účastníka pro přístup k síti, zatímco poskytovatel služby autentizuje uživatele pro přístup k aplikaci.

Toto řeší kritické problémy obchodní autonomie, bezpečnostního oddělení a provozní složitosti. Umožňuje nové modely poskytování služeb více stranami, jako je network slicing pro podniky, kde uživatel slicu (podnik) spravuje přístup ke slicu, a usnadňuje konvergenci pevného a mobilního přístupu se společným AAA bodem v síti služeb.

## Klíčové vlastnosti

- Poskytuje AAA služby externí vůči doméně důvěry 3GPP
- Spolupracuje s 5GC přes SMF nebo NEF pomocí standardizovaných procedur
- Podporuje protokoly Diameter a RADIUS pro interoperabilitu
- Umožňuje nezávislé vynucování politik operátorem datové sítě
- Umožňuje oddělenou správu přihlašovacích údajů od předplatného 3GPP
- Usnadňuje účtování a charging pro služby specifické pro DN

## Definující specifikace

- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping

---

📖 **Anglický originál a plná specifikace:** [DN-AAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/dn-aaa/)
