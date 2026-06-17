---
slug: "aoc-d"
url: "/mobilnisite/slovnik/aoc-d/"
type: "slovnik"
title: "AOC-D – Advice Of Charge - During the communication"
date: 2026-01-01
abbr: "AOC-D"
fullName: "Advice Of Charge - During the communication"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aoc-d/"
summary: "AOC-D je služba 3GPP, která poskytuje uživateli informace o účtování v reálném čase během aktivní komunikační relace, jako je hovor nebo datová relace. Umožňuje uživatelům sledovat narůstající poplatk"
---

AOC-D je služba 3GPP, která poskytuje uživateli informace o účtování v reálném čase během aktivní komunikační relace, což mu umožňuje sledovat narůstající poplatky.

## Popis

Advice Of Charge - During the communication (AOC-D) je standardizovaná služba v rámci specifikací 3GPP, která doručuje uživateli informace související s účtováním během probíhající komunikační relace. Funguje jako součást širší rodiny doplňkových služeb Advice of Charge (AoC), která zahrnuje také [AOC-E](/mobilnisite/slovnik/aoc-e/) (na konci relace) a [AOC-S](/mobilnisite/slovnik/aoc-s/) (pro speciální služby). AOC-D je konkrétně navržena tak, aby poskytovala periodické nebo událostmi spouštěné aktualizace o kumulovaných poplatcích během relace, jako je přepojování okruhů hlasového hovoru, paketově přepínaná datová relace nebo služba multimediální telefonie. Služba je implementována prostřednictvím interakcí mezi síťovými prvky, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) a Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)), což zajišťuje, že data o účtování jsou shromažďována, zpracovávána a předávána do uživatelského zařízení téměř v reálném čase.

Z architektonického hlediska AOC-D využívá infrastrukturu pro účtování a signalizaci v jádrové síti. Pro služby s přepojováním okruhů se integruje s mechanismy účtování [CAMEL](/mobilnisite/slovnik/camel/) (Customized Applications for Mobile networks Enhanced Logic) nebo IMS (IP Multimedia Subsystem). Při zahájení relace síť spustí účtování na základě předdefinovaných tarifních modelů. Účtovací funkce, která často komunikuje s OCS v předplacených scénářích, monitoruje parametry využití, jako je délka hovoru, objem dat nebo události služby. V nakonfigurovaných intervalech nebo při splnění specifických podmínek (např. dosažení prahové hodnoty poplatku) síť vygeneruje zprávu AOC-D obsahující podrobnosti, jako je aktuální výše poplatku, měna a tarifní čas. Tato zpráva je poté přenesena do uživatelského zařízení (UE) pomocí signalizace v pásmu (např. pomocí prvků User-to-User Information v [ISUP](/mobilnisite/slovnik/isup/)) nebo metodami mimo pásmo (např. prostřednictvím zpráv SIP v IMS), v závislosti na typu služby a síťové architektuře.

Mezi klíčové komponenty zapojené do AOC-D patří UE, které musí podporovat schopnosti prezentace AOC-D pro zobrazení poplatků uživateli; MSC nebo Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) pro řízení relace a signalizaci; a účtovací systém (např. OCS nebo Charging Data Function (CDF)). Služba funguje tak, že účtovací systém vypočítá přírůstkové poplatky na základě dat o využití v reálném čase a instruuje uzel řízení relace, aby odeslal informaci do UE. Například u předplaceného hlasového hovoru OCS postupně odečítá kredit během hovoru a může spustit oznámení AOC-D, když kredit dosáhne varovných úrovní. Ve službách založených na IMS lze AOC-D implementovat pomocí zpráv SIP INFO nebo jako součást aktualizací Session Description Protocol (SDP), což umožňuje flexibilní integraci s multimediálními relacemi.

Úloha AOC-D v síti spočívá ve zlepšení uživatelského zážitku a provozní efektivity tím, že poskytuje transparentnost v účtování. Podporuje různé fakturační modely, včetně časového, objemového a událostního účtování, a je nezbytná pro splnění regulatorních požadavků v mnoha regionech. Služba také komunikuje s dalšími síťovými funkcemi, jako je řízení politik pro účtování s ohledem na QoS, což zajišťuje, že poplatky odpovídají poskytované kvalitě služby. Díky zpětné vazbě v reálném čase pomáhá AOC-D snižovat spory se zákazníky a podporovat kontrolu nákladů, zejména v roamingu, kde mohou být poplatky vyšší.

## K čemu slouží

AOC-D byla vytvořena, aby řešila potřebu transparentnosti účtování v reálném čase v telekomunikačních sítích, zejména když se služby vyvinuly za rámec jednoduchých hlasových hovorů a zahrnuly data a multimédia. Před jejím zavedením uživatelé často získávali informace o účtování až na konci relace (prostřednictvím AOC-E) nebo na periodických vyúčtováních, což vedlo k nepříjemným překvapením, jako je 'bill shock', když využití překročilo očekávání. To bylo zvláště problematické s nástupem mobilních dat a prémiových služeb, kde se náklady mohly rychle kumulovat. AOC-D to řeší poskytováním průběžných aktualizací během relace, což uživatelům umožňuje sledovat výdaje a činit informovaná rozhodnutí, například ukončit hovor nebo omezit využití dat.

Historicky motivace pro AOC-D vycházela z požadavků operátorů na zlepšení spokojenosti zákazníků a snížení fluktuace, stejně jako z regulatorních tlaků na jasnější fakturační postupy. Ve verzi 3GPP Release 7 byla standardizována jako součást širších vylepšení AoC pro podporu vznikajících služeb IMS a předplacených služeb. Služba řeší omezení předchozích přístupů integrací s online účtovacími systémy, což umožňuje dynamické aktualizace bez narušení relace. Pro operátory AOC-D usnadňuje lepší zajištění příjmů a snižuje náklady na podporu související s dotazy na účtování, zatímco uživatelům poskytuje kontrolu nad výdaji, zejména v předplaceném kontextu nebo při roamingu, kde je správa rozpočtu klíčová.

AOC-D dále podporuje vývoj směrem ke složitějším balíčkům služeb a síťovému slicingu v 5G, kde se účtování může lišit v závislosti na typu slice nebo QoS. Poskytováním informací v reálném čase pomáhá uživatelům pochopit nákladové důsledky různých úrovní služeb, což je v souladu s trendy personalizovaných a transparentních telekomunikačních nabídek. Služba také umožňuje inovativní případy užití, jako jsou rodičovské kontroly nebo firemní limity výdajů, tím, že umožňuje oznámení v reálném čase, která mohou spustit akce uživatele.

## Klíčové vlastnosti

- Aktualizace účtování v reálném čase během aktivních relací
- Podpora více typů služeb (hlas, data, multimedia)
- Integrace s Online Charging System (OCS) pro předplacené scénáře
- Flexibilní spouštěcí mechanismy (časové, objemové, událostní)
- Doručení prostřednictvím signalizace v pásmu nebo mimo pásmo (např. ISUP, SIP)
- Konfigurovatelné formáty prezentace na uživatelském zařízení

## Související pojmy

- [AOC-E – Advice Of Charge - at the End of the communication](/mobilnisite/slovnik/aoc-e/)
- [AOC-S – Advice Of Charge at communication Set-up time](/mobilnisite/slovnik/aoc-s/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.647** (Rel-19) — Advice of Charge (AOC) service protocol
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony

---

📖 **Anglický originál a plná specifikace:** [AOC-D na 3GPP Explorer](https://3gpp-explorer.com/glossary/aoc-d/)
