---
slug: "ab"
url: "/mobilnisite/slovnik/ab/"
type: "slovnik"
title: "AB – Access Barring"
date: 2025-01-01
abbr: "AB"
fullName: "Access Barring"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ab/"
summary: "Access Barring (AB – řízení přístupu) je síťově řízený mechanismus, který reguluje pokusy UE o přístup, aby zabránil stavům přetížení v mobilních sítích. Selektivně blokuje nebo zpožďuje žádosti o při"
---

AB (Access Barring – řízení přístupu) je síťově řízený mechanismus, který reguluje pokusy uživatelského zařízení o přístup, aby zabránil přetížení selektivním blokováním nebo zpožďováním žádostí o připojení na základě nastavených parametrů.

## Popis

Access Barring (AB – řízení přístupu) je základní mechanismus pro řízení zahlcení v sítích 3GPP, který funguje na vrstvě Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Když síť zaznamená vysoké zatížení nebo přejde do stavu přetížení, vysílá v blocích systémové informace (SIB) specifické parametry řízení přístupu, primárně SIB2 pro LTE a SIB14 pro specifické scénáře. Tyto parametry uživatelskému zařízení (UE) sdělují, zda má pokračovat v pokusu o přístup, nebo má uplatnit zpoždění. Základní mechanismus spočívá v tom, že UE vygeneruje náhodné číslo a porovná jej s vysílaným faktorem řízení (barring factor). Pokud je náhodné číslo nižší než tento faktor, je přístup zamítnut a UE musí před dalším pokusem počkat po stanovenou dobu řízení (barring time).

Architektura Access Barring je rozdělena mezi síťový Radio Access Network (RAN) a UE. Síťová strana, řízená eNodeB v LTE nebo gNB v 5G NR, určuje úroveň zahlcení a dynamicky nastavuje parametry řízení (např. ac-BarringFactor, ac-BarringTime) pro různé přístupové třídy. Tyto parametry jsou následně vysílány přes rozhraní vzduchu. Strana UE implementuje logiku řízení podle specifikace 3GPP TS 36.331 (protokol RRC). Při zahájení procedury navázání spojení (např. RRC Connection Request) entita RRC v UE vyhodnotí relevantní informace o řízení na základě své přístupové třídy, typu pokusu o přístup (mobile originating signaling, mobile originating data, emergency) a konkrétní přijaté konfigurace řízení.

Klíčové součásti mechanismu AB zahrnují faktor řízení (pravděpodobnostní hodnota mezi 0 a 1), dobu řízení (dobu, po kterou je přístup zakázán po rozhodnutí o řízení) a identifikátory přístupových tříd. UE jsou přiřazena k jedné z deseti náhodně přidělených běžných přístupových tříd (0-9) a mohou také patřit ke speciálním přístupovým třídám (11-15) pro prioritní uživatele, jako jsou operátoři sítí, záchranné služby nebo veřejné utility. Síť může vysílat samostatné parametry řízení pro běžné třídy a pro speciální třídy, což umožňuje rozdílné zacházení. Dále AB podporuje řízení pro specifické typy pokusů o přístup, například pouze signalizační nebo pouze datové pokusy, což poskytuje detailní kontrolu.

Při provozu hraje AB klíčovou roli v Radio Resource Management (RRM) a řízení přetížení. Omezováním rychlosti příchozích žádostí o připojení zabraňuje zahlcení RAN a uzlů core sítě (jako je [MME](/mobilnisite/slovnik/mme/) v LTE), což by mohlo vést k přerušeným hovorům, signalizačním bouřím nebo úplným výpadkům služeb. Tento mechanismus je obzvláště důležitý během nepředvídatelných událostí, které způsobí náhlý nárůst pokusů o přístup, například při přírodních katastrofách, kdy se mnoho uživatelů současně pokouší volat. AB zajišťuje, že síť zůstane funkční alespoň pro prioritní služby a může se postupně zotavit, jak se zatížení normalizuje.

## K čemu slouží

Access Barring (řízení přístupu) bylo zavedeno, aby vyřešilo kritický problém síťového zahlcení a přetížení, které se stávalo stále častějším s vývojem mobilních sítí od systémů orientovaných na hlas k systémům orientovaným na data s obrovským počtem připojených zařízení. Rané mobilní systémy měly omezené mechanismy pro zvládnutí náhlých špiček provozu, což často vedlo k úplnému kolapsu sítě během mimořádných událostí nebo velkých veřejných akcí. Primární motivací pro AB bylo poskytnout síti proaktivní, standardizovaný nástroj pro regulaci pokusů o přístup dříve, než zahlcení způsobí nevratné zhoršení služeb. Řeší základní výzvu sdílených rádiových prostředků: když příliš mnoho zařízení současně usiluje o přístup, dochází ke kolizím, neúspěšným procedurám a plýtvání signalizací, což v konečném důsledku poškozuje všechny uživatele.

Historicky, před standardizovanými mechanismy AB, se sítě spoléhaly na jednodušší, méně detailní přístupy, jako je tvrdé blokování nebo proprietární řešení specifická pro dodavatele, kterým často chyběla spravedlivost a diferenciace priorit. Vytvoření AB ve specifikaci 3GPP Release 5 (v rámci UMTS) stanovilo jednotnou pravděpodobnostní metodu, kterou lze dynamicky upravovat na základě stavu sítě v reálném čase. To byl významný vývoj oproti trvalé nebo polostatické kontrole přístupu. AB konkrétně řeší problém signalizačního přetížení na entitách řídicí roviny a zahlcení rádiového rozhraní, čímž zajišťuje, že se k nezbytným službám (jako jsou tísňová volání) lze stále dostat, i když je síť pod extrémním stresem.

Tato technologie existuje, aby vyvážila integritu sítě a práva uživatelů na přístup. Bez AB by síť čelící náhlému nárůstu požadavků (např. po výpadku proudu při obnově služby) mohla zažít 'signalizační bouři', kdy by se procesory core sítě přetížily, což by způsobilo kaskádové selhání. AB to zmírňuje tím, že distribuuje rozhodovací logiku na samotná UE pomocí vysílaných parametrů. Tento decentralizovaný přístup je efektivně škálovatelný, protože síť nemusí jednotlivě odmítat každou žádost; místo toho se UE samy regulují na základě společných pravidel. Dále AB poskytuje základ pro pokročilejší funkce řízení zahlcení zavedené v pozdějších releasech, jako jsou vylepšení Access Class Barring (ACB) a řízení přístupu specifické pro aplikace.

## Klíčové vlastnosti

- Pravděpodobnostní řízení přístupu pomocí vysílaných faktorů řízení a porovnávání náhodných čísel
- Diferencované řízení pro více přístupových tříd (0-9 běžné, 11-15 speciální)
- Detailní kontrola nad typy pokusů o přístup (např. mobile originating signaling, data, emergency)
- Dynamické nastavování parametrů sítí na základě podmínek zatížení v reálném čase
- Vynucování doby řízení, aby se zabránilo okamžitým opakovaným pokusům a rozložilo zatížení
- Podpora prioritizace tísňových služeb pomocí samostatných parametrů řízení

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [AB na 3GPP Explorer](https://3gpp-explorer.com/glossary/ab/)
