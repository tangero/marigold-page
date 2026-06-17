---
slug: "oplmn"
url: "/mobilnisite/slovnik/oplmn/"
type: "slovnik"
title: "OPLMN – Operator Controlled PLMN (Selector List)"
date: 2025-01-01
abbr: "OPLMN"
fullName: "Operator Controlled PLMN (Selector List)"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/oplmn/"
summary: "Seznam PLMN řízený operátorem (OPLMN) je seznam preferovaných veřejných pozemních mobilních sítí (PLMN) uložený na SIM/USIM uživatelského zařízení (UE). Poskytuje jej domovský operátor, aby usměrňoval"
---

OPLMN je seznam preferovaných sítí poskytnutý operátorem a uložený na SIM/USIM, který usměrňuje výběr sítě zařízení, zejména při roamingu, aby upřednostnil partnerské sítě pro spolehlivé služby a kontrolované náklady.

## Popis

Seznam PLMN řízený operátorem (OPLMN) je důležitý soubor ([EF](/mobilnisite/slovnik/ef/)_OPLMNwACT) uložený na univerzálním identifikačním modulu účastníka (USIM) nebo SIM kartě uživatelského zařízení (UE). Obsahuje seznam kódů veřejných pozemních mobilních sítí (PLMN) seřazený podle priority, který má UE použít během procesu výběru a registrace sítě, zejména když je mimo pokrytí své domovské PLMN ([HPLMN](/mobilnisite/slovnik/hplmn/)). OPLMN se liší od seznamu PLMN řízeného uživatelem; je zřízen a aktualizován mobilním operátorem, nikoli koncovým uživatelem, což dává operátorovi kontrolu nad roamingovým zážitkem.

Z technického hlediska je seznam OPLMN uložen jako posloupnost záznamů, z nichž každý obsahuje kód PLMN ([MCC](/mobilnisite/slovnik/mcc/)+[MNC](/mobilnisite/slovnik/mnc/)) a přidružený identifikátor 'přístupové technologie'. Pole přístupové technologie (např. [E-UTRAN](/mobilnisite/slovnik/e-utran/), UTRAN, [GERAN](/mobilnisite/slovnik/geran/), NR) určuje preferovanou technologii rádiového přístupu pro danou PLMN. Když je UE zapnuto nebo ztratí pokrytí, provede proceduru výběru sítě definovanou v TS 23.122. Nejprve se pokusí najít a zaregistrovat se ve své HPLMN. Pokud to selže (tj. při roamingu), UE se obrátí na seznam OPLMN. Prohledá dostupné sítě a pokusí se zaregistrovat v PLMN s nejvyšší prioritou ze seznamu OPLMN, kterou najde a která umožňuje přístup. UE používá přidružený identifikátor přístupové technologie k upřednostnění svého hledání; například bude hledat buňku 5G NR od preferovaného partnera dříve, než bude hledat buňku 4G LTE od stejného partnera.

OPLMN funguje ve spojení s dalšími seznamy na USIM, konkrétně s HPLMN, seznamem PLMN řízeným uživatelem (UPLMN) a seznamem zakázaných PLMN ([FPLMN](/mobilnisite/slovnik/fplmn/)). Standardní priorita výběru je: HPLMN, poté seznam OPLMN (v pořadí podle priority), poté seznam UPLMN a poté další dostupné sítě podle síly signálu. Seznam FPLMN obsahuje sítě, na které je UE dočasně zakázáno se registrovat kvůli předchozímu odmítnutí. Operátoři dynamicky aktualizují seznam OPLMN prostřednictvím dálkové správy SIM ([OTA](/mobilnisite/slovnik/ota/)), což jim umožňuje měnit roamingová partnerství, přidávat nové preferované sítě v navštívené zemi nebo snížit prioritu sítí se špatnou kvalitou služeb nebo vysokými náklady, a to vše bez zásahu uživatele.

## K čemu slouží

OPLMN byl vytvořen, aby vyřešil základní problém nekontrolovaného výběru sítě během roamingu, který existoval v raných celulárních systémech. Bez seznamu poskytnutého operátorem by roamingové UE typicky vybíralo síť pouze na základě síly rádiového signálu z dostupných sítí v navštívené zemi. To mohlo vést k několika problémům: UE se mohlo připojit k síti bez roamingové dohody, což vedlo k neúspěšné registraci a odmítnutí služby. I když dohoda existovala, připojení k první dostupné síti nemuselo být z pohledu operátora optimální volbou, protože se mohlo jednat o dražšího partnera, nabízet horší kvalitu služeb nebo postrádat podporu určitých služeb, jako jsou data nebo IMS.

Hlavním účelem OPLMN je dát domovskému síťovému operátorovi komerční a technickou kontrolu nad roamingovým zážitkem svých účastníků. Zajišťuje spolehlivou a automatickou dostupnost služeb nasměrováním účastníků na sítě s ověřenými roamingovými dohodami. Umožňuje operátorům implementovat strategie kontroly nákladů upřednostňováním partnerů s nižšími velkoobchodními sazbami. Dále umožňuje správu kvality služeb směrováním účastníků na sítě, které podporují požadované technologie (např. 4G/5G pro datové služby) nebo mají prokázané smlouvy o úrovni služeb (SLA). Předkonfigurací tohoto seznamu operátor zaručuje uživateli při cestování plynulý zážitek 'jako doma', protože se zařízení automaticky připojí k nejlepší dostupné partnerské síti bez nutnosti ručního výběru sítě uživatelem.

## Klíčové vlastnosti

- Prioritizovaný seznam kódů PLMN zřízený operátorem a uložený na USIM/SIM
- Pro každou PLMN obsahuje přidruženou preferovanou přístupovou technologii (např. NR, E-UTRAN)
- Používá se UE během automatického výběru sítě, zejména v roamingových scénářích
- Má přednost před seznamy řízenými uživatelem a výběrem založeným na síle signálu
- Lze jej dynamicky aktualizovat operátorem prostřednictvím dálkové správy SIM (OTA)
- Funguje spolu se seznamy HPLMN, UPLMN a FPLMN v definované hierarchii výběru

## Související pojmy

- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [FPLMN – Forbidden Public Land Mobile Network](/mobilnisite/slovnik/fplmn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [OPLMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/oplmn/)
