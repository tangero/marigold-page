---
slug: "pop-nm"
url: "/mobilnisite/slovnik/pop-nm/"
type: "slovnik"
title: "POP-NM – Participating Operator Network Manager"
date: 2025-01-01
abbr: "POP-NM"
fullName: "Participating Operator Network Manager"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pop-nm/"
summary: "Funkce Network Manager pro Participating Operator v prostředí více operátorů. Poskytuje komplexní (end-to-end) schopnosti správy sítě pro vlastní zdroje operátora a koordinuje s nadřazenými manažery v"
---

POP-NM je funkce Network Manager pro Participating Operator, která spravuje jeho vlastní zdroje a koordinuje s nadřazenými manažery v prostředí sdílené infrastruktury více operátorů.

## Popis

Participating Operator Network Manager (POP-NM) je komplexní systém správy sítě definovaný ve specifikaci 3GPP TS 32.130. Představuje nejvyšší řídicí entitu pro celou síťovou doménu Participating Operatora v rámci architektury spolupráce více operátorů. Na rozdíl od Domain Manageru ([DM](/mobilnisite/slovnik/dm/)), který se zaměřuje na konkrétní doménu (např. RAN nebo Core), má POP-NM širší rozsah působnosti a může dohledávat více DM (např. [POP-RAN-DM](/mobilnisite/slovnik/pop-ran-dm/) a [POP-CORE-DM](/mobilnisite/slovnik/pop-core-dm/)) v rámci administrativní hranice Participating Operatora. Jeho úlohou je poskytovat integrovanou, komplexní (end-to-end) správu zdrojů, které operátor přispívá, a zajistit, aby fungovaly jako kohezní celek pro poskytování služeb slíbených nadřazené řídicí entitě (např. Master Network Manageru).

Z hlediska architektury se POP-NM nachází v hierarchii správy mezi nadřazeným Network Managerem (např. hostujícího operátora nebo tenanta síťového řezu) a Domain Managery v rámci vlastní organizace Participating Operatora. Pro komunikaci s nadřazeným [NM](/mobilnisite/slovnik/nm/) používá referenční bod Itf-N. Interně může používat Itf-N nebo jiná rozhraní pro komunikaci se svými podřízenými DM. POP-NM je zodpovědný za správu služeb, včetně překladu požadavků na komplexní služby (jako jsou [SLA](/mobilnisite/slovnik/sla/) pro síťový řez) na doménově specifické politiky a konfigurační příkazy, které distribuuje svým DM. Provádí konsolidovanou korelaci chyb, analýzu hlavní příčiny napříč svými doménami a agreguje výkonnostní data pro hlášení směrem nahoru.

Operačně POP-NM zvládá životní cyklus služeb, které pokrývají zdroje Participating Operatora. Spravuje aktivaci, modifikaci, zajištění (assurance) a vyřazení těchto služeb. Je klíčovým bodem pro implementaci správy založené na politikách, zajištění prosazování bezpečnostních politik napříč svými doménami a koordinaci přidělování zdrojů mezi částmi RAN a CN pod jeho kontrolou. Tím, že působí jako jediný kontaktní a řídicí bod pro nadřazený NM, POP-NM zjednodušuje složitost správy více dodavatelů a více domén pro externí entitu a prezentuje jednotný pohled na správu síťových aktiv, která Participating Operator přispívá.

## K čemu slouží

POP-NM byl vytvořen, aby naplnil potřebu řízeného, hierarchického přístupu v komplexních partnerstvích více operátorů, jako jsou například partnerství vyžadovaná pro národní roaming, hostování mobilního virtuálního operátora ([MVNO](/mobilnisite/slovnik/mvno/)) nebo sdílení infrastruktury. Před jeho standardizací správa takovýchto spoluprácí často zahrnovala ad-hoc integrace, vlastní rozhraní a rozmazané hranice odpovědnosti, což vedlo k provozní neefektivitě a sporům. POP-NM poskytuje standardizovanou roli a rozhraní, aby mohl operátor vystupovat jako autonomní poskytovatel služeb v rámci většího ekosystému.

Jeho primárním účelem je umožnit Participating Operatorovi zachovat celkovou kontrolu a přehled o vlastní síti a zároveň bezproblémově integrovat jeho řídicí rovinu s řídicí rovinou partnera nebo nadřazené entity. Řeší problém, jak delegovat odpovědnost za správu celé sítě operátora, nejen jedné domény, způsobem, který je škálovatelný a bezpečný. POP-NM umožňuje Participating Operatorovi nabízet svou síť jako spravovanou službu s dobře definovanými hranicemi služeb a jasnou odpovědností za plnění [SLA](/mobilnisite/slovnik/sla/). Motivací pro jeho vývoj spolu s dalšími funkcemi správy [POP](/mobilnisite/slovnik/pop/) ve verzi 12 byl posun průmyslu směrem k flexibilnějším a dynamičtějším modelům sdílení sítí, které vyžadovaly robustní, standardizovaný rámec správy, aby byly takové spolupráce komerčně a technicky životaschopné.

## Klíčové vlastnosti

- Komplexní (end-to-end) správa služeb pro síťové zdroje Participating Operatora
- Agregace a korelace dat o chybách a výkonu z více Domain Managerů
- Orchestrace politik a překlad mezi požadavky nadřazeného NM a interními doménovými příkazy
- Jediný kontaktní bod pro nadřazený Network Manager prostřednictvím rozhraní Itf-N
- Správa životního cyklu kompozitních služeb pokrývajících domény RAN a Core
- Jednotné prosazování bezpečnostních politik a politik napříč spravovanými doménami operátora

## Související pojmy

- [POP-CORE-DM – Participating Operator Core Network Domain Manager](/mobilnisite/slovnik/pop-core-dm/)
- [POP-RAN-DM – Participating Operator Radio Access Network Domain Manager](/mobilnisite/slovnik/pop-ran-dm/)

## Definující specifikace

- **TS 32.130** (Rel-19) — Network Sharing OAM&P Requirements

---

📖 **Anglický originál a plná specifikace:** [POP-NM na 3GPP Explorer](https://3gpp-explorer.com/glossary/pop-nm/)
