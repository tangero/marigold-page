---
slug: "nrr"
url: "/mobilnisite/slovnik/nrr/"
type: "slovnik"
title: "NRR – Non-Aggregated RUCI Report Request"
date: 2025-01-01
abbr: "NRR"
fullName: "Non-Aggregated RUCI Report Request"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nrr/"
summary: "Žádost o podrobnou zprávu o využití prostředků a informacích o zahlcení (RUCI) v přístupové síti (RAN) pro jednotlivá uživatelská zařízení (UE). Umožňuje síti shromažďovat podrobná data o využití rádi"
---

NRR je žádost o podrobnou zprávu o využití prostředků a informacích o zahlcení (RUCI) pro každé uživatelské zařízení (UE) z přístupové sítě (RAN) pro podporu správy a optimalizace provozu.

## Popis

Non-Aggregated [RUCI](/mobilnisite/slovnik/ruci/) Report Request (NRR) je řídicí procedura a typ zprávy definovaný ve specifikacích 3GPP pro [E-UTRAN](/mobilnisite/slovnik/e-utran/) a NG-RAN. Je iniciována síťovou řídicí entitou, typicky Element Managerem ([EM](/mobilnisite/slovnik/em/)) nebo Network Managerem ([NM](/mobilnisite/slovnik/nm/)), směrem k uzlu přístupové sítě (RAN), jako je [eNB](/mobilnisite/slovnik/enb/) nebo gNB, přes rozhraní Itf-N. Žádost přikazuje uzlu RAN vygenerovat a odeslat zprávu obsahující podrobné, neagregované informace o využití prostředků a zahlcení (RUCI). Na rozdíl od agregovaných zpráv, které poskytují sumarizovaná data, obsahuje neagregovaná zpráva jemně strukturované informace, často na úrovni jednotlivých uživatelských zařízení (UE) nebo specifických prostředků, což umožňuje hlubokou diagnostiku a cílenou optimalizaci.

Proces generování zprávy je spuštěn po přijetí příkazu NRR. Uzel RAN shromažďuje požadovaná data RUCI ze svých interních měření a čítačů. Tato data mohou zahrnovat metriky jako využití fyzických bloků prostředků ([PRB](/mobilnisite/slovnik/prb/)), délky front plánovače, počet aktivních UE, úspěšnost předávání spojení a indikátory zahlcení pro konkrétní buňky, síťové řezy nebo toky QoS. Klíčovým aspektem kvalifikátoru 'Non-Aggregated' je, že data nejsou sumarizována napříč velkým souborem UE nebo dlouhým časovým oknem; místo toho mohou poskytovat snímky nebo časové řady pro jednotlivé entity. Shromážděná data jsou poté naformátována do zprávy (Non-Aggregated RUCI Report) a odeslána zpět vyžadujícímu řídicímu systému.

Role NRR je klíčová pro správu výkonu, správu poruch a funkce samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)). Získáním neagregovaných dat mohou operátoři sítí a řídicí systémy provádět analýzu hlavní příčiny událostí zahlcení, porozumět vzorcům spotřeby prostředků konkrétních uživatelů nebo služeb s vysokou poptávkou a ověřovat účinnost změn konfigurace sítě. Poskytuje viditelnost potřebnou pro pokročilé směrování provozu, plánování kapacity a vynucování QoS, zejména ve složitých scénářích zahrnujících síťové řezy a různé požadavky služeb. Procedura je součástí širšího rámce zajištění výkonu ([PA](/mobilnisite/slovnik/pa/)) a správy konfigurace (CM) definovaného 3GPP pro automatizovaný provoz a údržbu sítě.

## K čemu slouží

NRR bylo zavedeno pro řešení potřeby podrobné, na požádání dostupné viditelnosti do výkonu a stavu prostředků rádiové přístupové sítě, kterou agregovaná výkonnostní měření nemohla poskytnout. Před jeho standardizací se síťové řídicí systémy často spoléhaly na předdefinované, agregované čítače (PM čítače), které nabízely pohled na vysoké úrovni, ale postrádaly podrobnost nutnou k diagnostice konkrétních problémů, jako je jediné UE způsobující zahlcení nebo konkrétní síťový řež trpící nedostatkem prostředků. Vytvoření procedury NRR bylo motivováno rostoucí složitostí mobilních sítí, zavedením síťových řezů v 5G a požadavkem na sofistikovanější schopnosti SON a analytiky.

Řeší problém neprůhledného výkonu RAN během konkrétních událostí nebo pro konkrétní entity. Tím, že umožňuje řídicímu systému vyžádat si podrobnou zprávu pro konkrétní buňku, skupinu UE nebo během konkrétního časového intervalu, mohou operátoři proaktivně spravovat zdraví sítě a kvalitu služeb. To je obzvláště důležité pro zajištění dodržování smlouvy o úrovni služeb (SLA) pro síťové řezy a pro odstraňování problémů, které zažívají zákazníci. NRR poskytuje flexibilní, dotazovací mechanismus pro extrakci přesných dat potřebných k analýze, což přesahuje omezení pevného, periodického reportování a umožňuje dynamičtější a efektivnější přístup ke správě výkonu RAN.

## Klíčové vlastnosti

- Spouští generování podrobné, neagregované zprávy o využití prostředků a zahlcení
- Je vyžadována řídicími systémy (EM/NM) od uzlů RAN (eNB/gNB) přes rozhraní Itf-N
- Poskytuje podrobná data, potenciálně pro každé UE nebo jednotku prostředku, na rozdíl od agregovaných PM dat
- Podporuje reportování na požádání a potenciálně spouštěné událostmi pro cílené šetření
- Nezbytné pro pokročilou síťovou analytiku, analýzu hlavní příčiny a monitorování SLA pro síťové řezy
- Integruje se do rámců správy výkonu (PM) a samoorganizujících se sítí (SON) definovaných 3GPP

## Definující specifikace

- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.217** (Rel-19) — Policy and Charging Control (PCC) for Np Interface

---

📖 **Anglický originál a plná specifikace:** [NRR na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrr/)
