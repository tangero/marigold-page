---
slug: "admc"
url: "/mobilnisite/slovnik/admc/"
type: "slovnik"
title: "ADMC – Automatically Detected and Manually Cleared"
date: 2025-01-01
abbr: "ADMC"
fullName: "Automatically Detected and Manually Cleared"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/admc/"
summary: "ADMC je klasifikace správy poruch pro síťové alarmy, kde je detekce automatizovaná, ale řešení vyžaduje manuální zásah. Představuje klíčovou kategorii v standardizovaném rámci správy alarmů 3GPP, kter"
---

ADMC je klasifikace poruch pro síťové alarmy, kdy je porucha detekována automaticky, ale k jejímu vyřešení je nutný manuální zásah.

## Popis

Automatically Detected and Manually Cleared (ADMC) je základní klasifikace v rámci rámce správy poruch (Fault Management, [FM](/mobilnisite/slovnik/fm/)) 3GPP definovaná v řadě technických specifikací (TS). Kategorizuje síťové poruchy nebo alarmy na základě jejich mechanismů detekce a vyřešení. Alarm ADMC je takový, kdy je poruchový stav automaticky identifikován monitorovacími systémy sítě – typicky prostřednictvím překročení výkonnostních prahových hodnot, detekce protokolových chyb nebo indikátorů selhání hardwaru – ale k vyřešení této poruchy je nutný manuální zásah personálu provozu a údržby (O&M).

Architektura podporující klasifikaci ADMC je zabudována do systémů provozu, správy a údržby (OAM) jak v rádiové přístupové síti (RAN), tak v síti jádra (CN). Mezi klíčové komponenty patří správci síťových prvků ([NE](/mobilnisite/slovnik/ne/)), kteří generují nezpracovaná hlášení alarmů, a systém správy prvků ([EMS](/mobilnisite/slovnik/ems/)) nebo systém správy sítě ([NMS](/mobilnisite/slovnik/nms/)), který tyto alarmy zpracovává, kategorizuje a prezentuje podle standardizovaných klasifikací závažnosti a typu vyřešení, jako je ADMC. Proces začíná nepřetržitým monitorováním klíčových výkonnostních ukazatelů ([KPI](/mobilnisite/slovnik/kpi/)), stavu hardwaru a softwarových procesů. Když je splněna předdefinovaná poruchová podmínka (např. selhání spoje, porucha desky nebo výrazné zhoršení výkonu), síťový prvek aktivuje hlášení alarmu. Toto hlášení obsahuje atributy jako identifikátor alarmu, vnímanou závažnost (Kritický, Závažný, Méně závažný, Varování), pravděpodobnou příčinu a navrhovaný typ vyřešení – v tomto případě ADMC.

Jakmile je alarm klasifikován jako ADMC, vstoupí do specifického pracovního postupu v rámci síťového operačního centra (NOC). Alarm je zaznamenán v systému správy poruch se stavem indikujícím potřebu manuální pozornosti. Objeví se na konzolích operátorů, často filtrován a prioritizován spolu s dalšími alarmy ADMC a automaticky řešenými alarmy. Proces manuálního vyřešení zahrnuje technika nebo inženýra diagnostikujícího hlavní příčinu, což může vyžadovat fyzickou kontrolu, výměnu hardwaru, komplexní rekonfiguraci nebo softwarové záplaty – tedy akce, které nelze bezpečně nebo spolehlivě automatizovat. Po provedení nápravné akce musí operátor alarm v systému správy ručně potvrdit a vyřešit, čímž aktualizuje jeho stav a často poskytne komentář k uzavření.

Role ADMC v síti je klíčová pro udržení kvality služeb a efektivního provozu. Poskytuje jasnou demarkační linii mezi poruchami, které mohou být řešeny autonomně samoléčícími mechanismy (jako alarmy [ADAC](/mobilnisite/slovnik/adac/) – Automatically Detected and Automatically Cleared), a těmi, které vyžadují lidskou expertizu. Tato klasifikace pomáhá při alokaci zdrojů, automatizaci procesů a provozní efektivitě. Standardizací této kategorie napříč specifikacemi 3GPP, jako jsou TS 28.111 a TS 32.111, je zajištěna interoperabilita mezi různými dodavateli a konzistentní postupy pro manipulaci s alarmy pro síťové operátory spravující složité heterogenní sítě.

## K čemu slouží

Klasifikace ADMC byla vytvořena, aby vnesla strukturu a standardizaci do chaotického světa správy síťových poruch. Před jejím formalizováním ve verzi 3GPP Release 8 bylo zacházení s alarmy z velké části specifické pro jednotlivé dodavatele s nekonzistentními definicemi metod detekce a vyřešení. To činilo správu sítí s více dodavateli neefektivní, náchylnou k chybám a náročnou na zdroje. Operátoři se potýkali s automatizací procesů nebo efektivním školením personálu, když každý síťový prvek používal pro podobné poruchy odlišnou terminologii a pracovní postupy.

Primární problém, který ADMC řeší, je jasná kategorizace poruch, které, ačkoli je lze detekovat automatizovanými monitorovacími systémy, k jejich vyřešení inherentně vyžadují lidský úsudek, fyzickou akci nebo komplexní rozhodování. Nelze a není vhodné všechny poruchy řešit automaticky; některé zásahy nesou riziko přerušení služby nebo vyžadují specializované znalosti. Definováním ADMC jako standardního typu vyřešení umožnilo 3GPP vývoj standardizovaných rozhraní OAM, formátů hlášení alarmů a provozních postupů. To umožňuje systémům správy sítě ([NMS](/mobilnisite/slovnik/nms/)) inteligentně směrovat alarmy, přiřazovat tikety správným podpůrným týmům a generovat přesné reporty o střední době do opravy (MTTR) pro manuálně řešené poruchy.

Historicky vycházela motivace z úsilí telekomunikačního průmyslu směrem k rámci správy telekomunikačních sítí (TMN) a zvýšení provozní efektivity. Jak se sítě s nasazením 3G a 4G stávaly složitějšími, objem alarmů exponenciálně rostl. Rozlišování mezi automaticky a manuálně řešenými alarmy se stalo nezbytným pro stanovení priorit pracovní zátěže operátorů a investice do automatizace tam, kde přinášela největší návratnost. ADMC spolu s dalšími kategoriemi, jako je [ADAC](/mobilnisite/slovnik/adac/) (Automatically Detected and Automatically Cleared), vytvořilo páteř racionalizovaného, efektivního procesu správy poruch, který je klíčový pro dosažení vysoké dostupnosti sítě a snížení provozních výdajů.

## Klíčové vlastnosti

- Standardizovaná klasifikace vyřešení alarmů v rámci rámce správy poruch (FM) 3GPP
- Vyžaduje manuální zásah personálu provozu a údržby (O&M) k vyřešení poruchy
- Integrální součást hlášení alarmů v rozhraní Itf-N a dalších rozhraních OAM
- Umožňuje konzistentní správu pracovních postupů pro poruchy napříč sítěmi s více dodavateli
- Podporuje stanovení priorit pracovní zátěže operátorů a alokaci zdrojů
- Umožňuje přesné reportování o časech manuálních oprav a provozní efektivitě

## Definující specifikace

- **TS 28.111** (Rel-19) — Fault Management Service Specification
- **TS 28.545** (Rel-17) — Fault Supervision for 5G Networks
- **TS 32.111** (Rel-19) — Fault Management Requirements
- **TS 32.541** (Rel-19) — SON Self-Healing Concepts and Requirements
- **TS 32.859** (Rel-12) — Alarm Management Quality Improvement Study

---

📖 **Anglický originál a plná specifikace:** [ADMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/admc/)
