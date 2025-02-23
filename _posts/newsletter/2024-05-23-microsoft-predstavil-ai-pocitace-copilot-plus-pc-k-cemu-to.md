---
author: Patrick Zandl
categories:
- Patrickův newsletter
- Apple
- Microsoft
- AI
- Internet
- Bezpečnost
- EU
- Automotive
date: '2024-05-23'
layout: post
original_newsletter: "#76 \U0001F9D1‍\U0001F4BB K čemu všechna ta AI v počítačích
  je?"
summary_points:
- Copilot Plus PC jsou nové AI počítače od Microsoftu, reagující na Apple.
- Recall je průlomová funkce, která nahrává obrazovku a analyzuje činnost uživatele
  pomocí AI.
- Analýza Recall probíhá lokálně na počítači, což má zajistit bezpečnost dat.
- Existují obavy ohledně soukromí a bezpečnosti dat funkce Recall, vzhledem k historii
  Microsoftu.
title: 'Microsoft představil AI počítače: Copilot Plus PC! K čemu to?'
---

Další květnová novinka je znovu navázaná na AI. Microsoft představil své AI počítače Copilot Plus PC. Sice tak učinil pár dní po představení nových Ipadů vybavený AI procesory, takže to svádí k prohlášení, že tak Microsoft jen reaguje na to, co udělalo Apple. Jenže minimálně podle vzhledu má Microsoft celou integraci dobře promyšlenou a je v ní významně dále, než co jsme viděli od Apple v polovině května. Nechci přitom zpochybňovat výkonnost produktového oddělení Microsoftu, ale neřekl bych, že tohle spíchli za ten týden. 

Podstatné totiž není to, že do nějakého PCčka nacpali AI procesor, který zvládá rychle odbavovat AI úlohy. Ani vás nebudu obtěžovat parametry tohoto procesoru (jo, ta sestava má 40 TOPS a více, ale to většině z nás bude fuk). Podstatné je, co z toho Microsoft vytěží. 

Potenciálně průlomovou funkcí je totiž **Recall.** Pokud to operačnímu systému dovolíte, průběžně nahrává vaši obrazovku a pomocí AI (to je ten vytížený procesor!) analyzuje, co tam děláte. A chápe, že třeba kreslíte nějaký obrázek, nejenom si ukládá ten obrázek, ale chápe, co děláte. No a když později potřebujete najít ten obrázek lahve, co jste kreslili, tak si nemusíte pamatovat jméno, pod kterým jste ho uložili, ale zeptat se Recallu na obrázky lahví, co jste včera kreslili. 

Všechno tohle probíhá a je analyzováno na vašem počítači, data se nikam nepřenášejí, čili to má být bezpečné. A Microsoft se zaklíná, že nový Copilot+ PC je nejbezpečnější počítač všech dob 😇. Podrobný [popis pro zájemce je zde](https://learn.microsoft.com/en-us/windows/ai/apis/recall). 

[![](https://substack-post-media.s3.amazonaws.com/public/images/834368ed-c6bd-4c51-a305-41c0c904d6bb.heic)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F834368ed-c6bd-4c51-a305-41c0c904d6bb.heic)Windows si dělají screenshoty a můžete se vracet v čase a vyhledávat, na čem jste pracovali. Díky AI také Recall pozná, co jste dělali a s čím atd. 

![](https://substack-post-media.s3.amazonaws.com/public/images/834368ed-c6bd-4c51-a305-41c0c904d6bb.heic)

Já musím říct, že podobný program jsem používal na Macu, [jmenuje se to Rewind](https://www.rewind.ai/) a nějak jsem tomu na chuť nepřišel. Ale to byla spíše časová osa, jejíž užitek byl pro mne maličký. Aby to umělo právě to kontextové vyhledávání s podporou AI, platí se za to dvacet dolarů měsíčně a jelikož se mi demo do mého pracovního workflow zařadit nepodařilo, tak jsem Rewind vzdal. Otázka zní, zda Microsoft má věc lépe dotaženou (AI NPU jistě pomůže) a zda zdarma to nebude použitelnější, než za tu dvacku. 

[![](https://substack-post-media.s3.amazonaws.com/public/images/428efcaa-0d28-4033-a525-9367eed5f02a.heic)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F428efcaa-0d28-4033-a525-9367eed5f02a.heic)Rewind pro Mac je velmi podobná aplikace, ovšem bez podpory AI procesoru. Zatím svět neuchvátila. 

![](https://substack-post-media.s3.amazonaws.com/public/images/428efcaa-0d28-4033-a525-9367eed5f02a.heic)

A samozřejmě se už vynořují obavy, že Recall bude noční můra pro soukromí. Inu, potenciálně ano. Ono je hezké, že veškerá data o tom, co jste za poslední dobu udělali, jsou uložená lokálně, ale pro hackery nebude asi tak těžké vám je sebrat. Pokud to není moc dobře uděláno. A v ochraně dat Microsoft nikdy moc neexceloval. Takže hezké články [o tom na Double Pulsar](https://doublepulsar.com/how-the-new-microsoft-recall-feature-fundamentally-undermines-windows-security-aa072829f218) ba [i na BBC](https://www.bbc.com/news/articles/cpwwqp6nx14o).